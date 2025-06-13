"""
Tourist Route Optimizer

This script allows the user to calculate and visualize an optimized walking route
between selected tourist attractions within a city using OpenStreetMap (OSM) data.

It computes the shortest path between locations, solves the Traveling Salesman Problem (TSP)
to find the most efficient visit order, and visualizes the route using Folium.

This script requires the following packages to be installed in your Python environment:
    * osmnx
    * networkx
    * folium
    * ortools

This file can also be imported as a module and contains the following functions:

    * load_graph - loads the walkable road network of a city from OSM
    * create_distance_matrix - calculates a distance matrix based on shortest paths
    * solve_tsp - solves the TSP to find the optimal visit sequence
    * plot_route - visualizes the route and saves it as an HTML map
"""

import osmnx as ox
import networkx as nx
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import folium

def load_graph(place_name):
    """
    Loads the street network graph for a given city or place.
    
    Parameters
    ----------
    place_name : str
        Name of the city or address
    
    Returns
    -------
    networkx.MultiDiGraph
        The street network graph
    """
    G = ox.graph_from_place(place_name, network_type='walk')
    return G

def create_distance_matrix(G, locations):
    """
    Creates a distance matrix between the given coordinates based on the shortest
    travel distance (in meters).
    
    Parameters
    ----------
    G : networkx.MultiDiGraph
        OSM street network graph
    locations : list of tuple
        List of (latitude, longitude) coordinates
    
    Returns
    -------
    list of list
        2D distance matrix in meters
    """
    node_ids = [ox.nearest_nodes(G, lon, lat) for lat, lon in locations]
    n = len(node_ids)
    matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                length = nx.shortest_path_length(G, node_ids[i], node_ids[j], weight='length')
                matrix[i][j] = length
            else:
                matrix[i][j] = 0
    return matrix

def solve_tsp(distance_matrix):
    """
    Solves the Traveling Salesman Problem (TSP) using Google OR-Tools.
    
    Parameters
    ----------
    distance_matrix :list of list
        Distance matrix
    
    Returns
    -------
    list
        Optimal visiting order (of indices)
    """
    tsp_size = len(distance_matrix)
    manager = pywrapcp.RoutingIndexManager(tsp_size, 1, 0)
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_idx, to_idx):
        return int(distance_matrix[manager.IndexToNode(from_idx)][manager.IndexToNode(to_idx)])
    
    transit_callback_idx = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_idx)
    
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    
    solution = routing.SolveWithParameters(search_parameters)
    
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        return route
    else:
        return []

def plot_route(G, locations, route, map_filename='route.html'):
    """
    Visualizes the route using Folium.
    
    Parameters
    ----------
    G : networkx.MultiDiGraph
        OSM street network graph
    locations : list of tuple
        Original coordinates [(lat, lon), ...].
    route : list 
        Visiting order of indices
    map_filename : str
        Name of the output HTML file
    
    Returns
    -------
    folium.Map
        The generated Folium map object
    """
    # Calculate the average latitude and longitude
    avg_lat = sum(lat for lat, lon in locations) / len(locations)
    avg_lon = sum(lon for lat, lon in locations) / len(locations)

    # Create the map centered at the average location
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=14)

    # Draw route lines
    node_ids = [ox.nearest_nodes(G, lon, lat) for lat, lon in locations]
    for i in range(len(route)-1):
        path = nx.shortest_path(G, node_ids[route[i]], node_ids[route[i+1]], weight='length')
        path_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
        folium.PolyLine(path_coords, color='blue', weight=3).add_to(m)

    # Add numbered markers
    for order, stop_index in enumerate(route[:-1]):
        lat, lon = locations[stop_index]
        folium.Marker(
            location=[lat, lon],
            popup=f"Stop {order + 1}",
            icon=folium.DivIcon(
                html=f"""<div style="font-size: 12pt; color: white; background: blue; border-radius: 50%; width: 28px; height: 28px; text-align: center; line-height: 28px;">{order + 1}</div>"""
        )
    ).add_to(m)

    m.save(map_filename)
    return m

