from dijkstra_with_pq import dijkstra_with_pq
from a_star import a_star

import time
import json

def FindShortestPath():
    with open('graphs/Test/berkshire/berkshire-latest.json','r') as fp:
        graph = json.load(fp)
    with open('graphs/Test/berkshire/pos.json','r') as ft:
        pos = json.load(ft)
    
    start = time.time()
    dijkstra_with_pq(graph, "218671", "5799753301", "length")
    end = time.time()
    print(end-start)
    
    start = time.time()
    a_star(graph, "218671", "5799753301", "length", pos)
    end = time.time()
    print(end-start)

FindShortestPath()
