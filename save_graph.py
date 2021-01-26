from osm2nx import read_osm
from clean_graph import clean_data
import json
import networkx as nx

G = read_osm('graphs/Test/berkshire/berkshire-latest.osm') #converts osm file to a network
pos = {k: (G.node[k]['lon'], G.node[k]['lat']) for k in G.nodes()} #gets the geocoordinates of all the nodes
print(len(pos))
G_dict = nx.to_dict_of_dicts(G) #converts network to adjacency dictionary
G_clean = clean_data(G_dict) #cleans the dictionary to have only relevent data

with open('graphs/Test/berkshire/berkshire-latest.json', 'w') as fp:
    json.dump(G_clean, fp)

with open('graphs/Test/berkshire/pos.json','w') as fw:
    json.dump(pos, fw)
