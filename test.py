import networkx as nx
import folium as fm
from sklearn.neighbors import KDTree
import pandas as pd

from clean_graph import clean_data
from dijkstra import dijkstra
from get_geocode import getGeoCode
from osm2nx import read_osm

G = read_osm('graphs/Test/map.osm') #converts osm file to a network
pos = {k: (G.node[k]['lon'], G.node[k]['lat']) for k in G.nodes()} #gets the geocoordinates of all the nodes
G_dict = nx.to_dict_of_dicts(G) #converts network to adjacency dictionary
G_clean = clean_data(G_dict) #cleans the dictionary to have only relevent data

start_address = 'Caversham Lawn Tennis Club'
end_address = 'Waitrose Caversham'

start = (float(getGeoCode(start_address)[0]), float(getGeoCode(start_address)[1]))
end = (float(getGeoCode(end_address)[0]), float(getGeoCode(end_address)[1])) #gets the geocoordinates of the source and destination addresses


#finds nearest node
nodes = pd.DataFrame.from_dict(pos, orient='index', columns=['y', 'x'])
tree = KDTree(nodes[['x','y']], metric='euclidean')
start_idx = tree.query([start], k=1, return_distance=False)[0]
closest_node_to_start = nodes.iloc[start_idx].index.values[0]
end_idx = tree.query([end], k=1, return_distance=False)[0]
closest_node_to_end = nodes.iloc[end_idx].index.values[0]



route_time = dijkstra(G_clean , closest_node_to_start , closest_node_to_end, 'time') #uses custom shortest path algorithm by time
route_length = dijkstra(G_clean, closest_node_to_start, closest_node_to_end, 'length') #uses custom shrtest path algorithm by length



graph_map = fm.Map(location=[51.4763,-0.9746], zoom_start=14, min_zoom=14)
graph_map.save("data/graph.html")



points_time = []
points_length = []


for node in route_time['path']:
    points_time.append(tuple([pos[node][1] , pos[node][0]]))
for node in route_length['path']:
    points_length.append(tuple([pos[node][1] , pos[node][0]]))

fm.Marker(location=start , icon=fm.Icon(color='red') , popup=start_address).add_to(graph_map)
fm.Marker(location=end , icon=fm.Icon(color='blue') , popup=end_address).add_to(graph_map)

graph_map.add_child(fm.PolyLine(locations=points_time,weight=5,color = 'red'))
graph_map.add_child(fm.PolyLine(locations=points_length,weight=5,color = 'blue'))

graph_map.save("data/graph_route.html")
