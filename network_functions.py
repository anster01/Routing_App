from get_geocode import getGeoCode
from crime_rating import FindCrimeRating
from find_nearest_node import NearestNode
from dijkstra import dijkstra
from dijkstra_with_pq import dijkstra_with_pq
from a_star import a_star
from bellman_ford import bellman_ford

from interactive_map import InteractiveMap, InteractiveCrimeMap

import pandas as pd
import folium as fm
import json


COLORS = ['green', 'black']

class Network_Functions:
    def __init__(self):
        self.addresses = []
        self.routes = []
        self.nearest_nodes = []
        self.coords = []
        self.route_lengths = []
        self.crime_rating = []

        with open('graphs/Test/pos.json','r') as fw:
            self.node_pos = json.load(fw)
        with open('graphs/Test/graph.json','r') as fp:
            self.graph = json.load(fp)
        with open('graphs/Test/graph_crime.json','r') as ft:
            self.graph_crime = json.load(ft)
        with open('crime_stats.json','r') as fs:
            self.crime_statistics = json.load(fs)
        
        
    def check_input(self):
        for location in self.addresses:
            try:
                geo_code = getGeoCode(location)
            except:
                geo_code = False
                self.coords.append(geo_code)
                
            if type(geo_code) == tuple:
                if geo_code[1] > -1.0080000 and geo_code[1] < -0.9412000 and geo_code[0] > 51.4595000 and geo_code[0] < 51.4931000:
                    self.coords.append(geo_code)
                else:
                    self.coords.append(False)

        
    def FindNearestNode(self):
        self.nearest_nodes += NearestNode(self.coords, self.node_pos)


    def FindShortestPath(self, weight):
        '''
        uncomment the algorithm you wish to use
        '''
        #route = dijkstra(self.graph, self.nearest_nodes[0], self.nearest_nodes[1], weight)
        #route = bellman_ford(self.graph, self.nearest_nodes[0], self.nearest_nodes[1], weight)
        #route = dijkstra_with_pq(self.graph, self.nearest_nodes[0], self.nearest_nodes[1], weight)
        route = a_star(self.graph, self.nearest_nodes[0], self.nearest_nodes[1], weight, self.node_pos)
        self.routes.append(route['path'])
        self.route_lengths.append(round(route['length'] / 1609.33,2))


    def FindShortestSafePath(self, weight):
        '''
        uncomment the algorithm you wish to use
        '''
        #self.routes.append(dijkstra(self.graph_crime, self.nearest_nodes[0], self.nearest_nodes[1],weight)['path'])
        #self.routes.append(bellman_ford(self.graph_crime, self.nearest_nodes[0], self.nearest_nodes[1],weight)['path'])
        #self.routes.append(dijkstra_with_pq(self.graph_crime, self.nearest_nodes[0], self.nearest_nodes[1],weight)['path'])
        self.routes.append(a_star(self.graph_crime, self.nearest_nodes[0], self.nearest_nodes[1],weight, self.node_pos)['path'])
            

    def FindRouteLengths(self):
        length = 0
        for node in range(len(self.routes[1])-1):
            length += self.graph[self.routes[1][node]][self.routes[1][node+1]]['length']
        length = round(length / 1609.33, 2)
        self.route_lengths.append(length)


    def GetCrimeRating(self):
        self.crime_rating = FindCrimeRating(self.routes, self.node_pos, self.crime_statistics)


    def DisplayMap(self):
        graph_map = fm.Map(location=[51.4763,-0.9746], zoom_start=14, min_zoom=14)

        points = [[] for i in range(len(self.routes))]
        idx = 0
        for route in self.routes:
            for node in route:
                points[idx].append((self.node_pos[node][1] , self.node_pos[node][0]))
            idx += 1

        fm.Marker(location=self.coords[0] , icon=fm.Icon(color='red') , popup='Start: '+self.addresses[0]).add_to(graph_map)
        fm.Marker(location=self.coords[-1] , icon=fm.Icon(color='blue') , popup='Destination: '+self.addresses[-1]).add_to(graph_map)

        idx = 1
        for route in points:
            graph_map.add_child(fm.PolyLine(locations=route, weight=4, popup = 'Length: '+str(self.route_lengths[0])+' miles\nTime: '+str(round(self.route_lengths[0]/3,1))+' hours', color = COLORS[idx]))
            idx -= 1

        graph_map.save("graph_route.html")

        window = InteractiveMap()
        window.show()

        return window


    def AvoidHighCrime(self):
        graph_map = fm.Map(location=[51.4763,-0.9746], zoom_start=14, min_zoom=14)

        crime_stats = pd.DataFrame.from_dict(self.crime_statistics)
        crime_stats = crime_stats.reset_index()
        crime_stats.columns = ['0', 'Number']

        graph_map.choropleth(geo_data='data/reading.json',
                      fill_color='YlOrRd',
                      fill_opacity=0.3,
                      line_opacity=0.5,
                      data = crime_stats,
                      columns = ['0', 'Number'],
                      key_on = 'feature.properties.SQUARE',
                      legend_name = 'Number of incidents')

        points = [[] for i in range(len(self.routes))]

        idx = 0
        for route in self.routes:
            for node in route:
                points[idx].append((self.node_pos[node][1] , self.node_pos[node][0]))
            idx += 1

        fm.Marker(location=self.coords[0] , icon=fm.Icon(color='red') , popup='Start: '+self.addresses[0]).add_to(graph_map)
        fm.Marker(location=self.coords[-1] , icon=fm.Icon(color='blue') , popup='Destination: '+self.addresses[-1]).add_to(graph_map)

        idx = 1
        idx2 = 0
        for route in points:
            graph_map.add_child(fm.PolyLine(locations=route,weight=2*(idx+2), popup = 'Length: '+str(self.route_lengths[idx2])+' miles\nTime: '+str(round(self.route_lengths[idx2]/3,2))+' hours\nCrime Rating: '+str(self.crime_rating[idx2]), color = COLORS[idx]))
            idx -= 1
            idx2 += 1

        graph_map.save("avoid_crime_route.html")

        window = InteractiveCrimeMap()
        window.show()

        return window
