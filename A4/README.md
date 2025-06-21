# A4: Modules, functions and imports
## Modular Route Optimization and Visualization with OSM Data

*Practice: Software Development (Python)*

**Author: Annabelle Kiefer**

---

For this assignment, I modularized and documented a **Python script** that calculates and visualizes an optimized walking route between selected tourist attractions in a city. I worked with **OpenStreetMap (OSM)** data and applied graph theory (via the **osmnx** and **networkx** libraries) as well as **Google's OR-Tools** to solve the Traveling Salesman Problem (TSP). The route is visualized using the **Folium** library and saved as an interactive HTML map. This will later help me in the final project on route optimization and its visualization.

---

## Features

- **Load** walkable street networks from OSM using `osmnx`
- **Compute** real-world distance matrices using `networkx`
- **Solve** the Traveling Salesman Problem (TSP) using Google OR-Tools
- **Visualize** optimized routes interactively with `folium`
- **Export** results as an HTML map for offline or browser viewing

---

## Requirements
### Setup Environment

```bash
# Create a new conda environment from the environment file
conda env create -f environment.yml

# Activate the environment
conda activate a4-env

# Launch Jupyter Notebook
jupyter notebook

