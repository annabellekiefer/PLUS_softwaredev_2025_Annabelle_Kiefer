# A3:Visualizing OSM Data in Salzburg with Folium

*Practice: Software Development (Python)*

**Author: Annabelle Kiefer**

---

For this assignment, I want to explore the **Folium** library and visualize some **OpenStreetMap (OSM)** data for the city of Salzburg. To extract POIs such as parks and cafes, I used the **osmnx** library.
This will later help me in the final project on route optimization and its visualization.

## Features

- **Load** walkable street networks of Salzburg from OSM using `osmnx`
- **Display** interactive city maps with custom tiles using `folium`
- **Extract** points of interest (POIs) like parks and cafés from OSM data
- **Add** custom markers for POIs directly on the map
  
---

## Requirements
### Setup Environment

```bash
# Create a new conda environment from the environment file
conda env create -f environmentA3.yml

# Activate the environment
conda activate A3Environment

# Launch Jupyter Notebook
jupyter notebook
