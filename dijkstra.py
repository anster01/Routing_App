def dijkstra(graph, start, end, weight):
    duration = {}
    pred = {}

    for node in graph.keys():
        duration[node] = float('Inf')
        pred[node] = ''
    duration[start] = 0
    all_nodes = list(graph)
    
    while len(all_nodes) > 0:
        shortest = duration[all_nodes[0]]
        shortest_node = all_nodes[0]
        for node in all_nodes:
            if (duration[node] < shortest):
                shortest = duration[node]
                shortest_node = node
        all_nodes.remove(shortest_node)
        for adjacent_node, adjacent_value in graph[shortest_node].items():
            if duration[adjacent_node] > duration[shortest_node] + adjacent_value[weight]: 
                duration[adjacent_node] = duration[shortest_node] + adjacent_value[weight]
                pred[adjacent_node] = shortest_node
    path = []
    node = end
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node) 
            node = pred[node] 
        else:
            break
    path.insert(0, start)
    return {'path': path, 'length': duration[end]}
