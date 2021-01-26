from priority_queue import Priority_Queue
from math import radians, cos, sin, asin, sqrt

def heuristic(start, end):
    lat1, lon1, lat2, lon2 = map(radians, [start[0], start[1], end[0], end[1]])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return c * 6000000

def a_star(graph, start, end, weight, pos):
    priority_queue = Priority_Queue()
    priority_queue.push([0,start])

    distance = {}
    pred = {}

    for node in graph.keys():
        distance[node] = float('Inf')
        pred[node] = ''
    distance[start] = 0

    while priority_queue.elements:
        current_node = priority_queue.pop()
        if current_node[1] == end:
            break
        for adjacent_node, adjacent_value in graph[current_node[1]].items():
            if distance[adjacent_node] > distance[current_node[1]] + adjacent_value[weight]:                
                distance[adjacent_node] = distance[current_node[1]] + adjacent_value[weight]
                priority = distance[adjacent_node] + adjacent_value[weight] + heuristic(pos[current_node[1]], pos[adjacent_node])
                priority_queue.push([priority, adjacent_node])
                pred[adjacent_node] = current_node[1]

    path = []
    node = end
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node) 
            node = pred[node] 
        else:
            break
    path.insert(0, start)
    return {'path': path, 'length': distance[end]}
