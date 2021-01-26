import json
from shapely.geometry import shape, Point

with open('crime_stats.json','r') as f:
    crime_stats = json.load(f)
with open('graphs/Test/graph.json','r') as f:
    graph_map = json.load(f)
with open('graphs/Test/pos.json','r') as f:
    node_pos = json.load(f)
with open('data/reading.json') as f:
    js = json.load(f)


for node in node_pos:
    point = Point(float(node_pos[node][0]), float(node_pos[node][1]))
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        #if node is in the shape
        if polygon.contains(point):
            #change the weights of arcs
            if crime_stats['0'][feature['properties']['SQUARE']] >= 11:
                for adjacent_node in graph_map[node]:
                    graph_map[node][adjacent_node]['length'] *= 2
            elif crime_stats['0'][feature['properties']['SQUARE']] <= 10 and crime_stats['0'][feature['properties']['SQUARE']] >= 9:
                for adjacent_node in graph_map[node]:
                    graph_map[node][adjacent_node]['length'] *= 1.8
            elif crime_stats['0'][feature['properties']['SQUARE']] <= 8 and crime_stats['0'][feature['properties']['SQUARE']] >= 7:
                for adjacent_node in graph_map[node]:
                    graph_map[node][adjacent_node]['length'] *= 1.6
            elif crime_stats['0'][feature['properties']['SQUARE']] <= 6 and crime_stats['0'][feature['properties']['SQUARE']] >= 4:
                for adjacent_node in graph_map[node]:
                    graph_map[node][adjacent_node]['length'] *= 1.4
            elif crime_stats['0'][feature['properties']['SQUARE']] <= 3 and crime_stats['0'][feature['properties']['SQUARE']] >= 2:
                for adjacent_node in graph_map[node]:
                    graph_map[node][adjacent_node]['length'] *= 1.2

with open('graphs/Test/graph_crime.json', 'w') as fp:
    json.dump(graph_map, fp)
