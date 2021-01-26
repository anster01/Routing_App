def bellman_ford(graph, start, end, weight):
    distance = {}
    pred = {}
    
    for node in graph.keys():
        distance[node] = float('Inf')
        pred[node] = ''
    distance[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for adjacent_node in graph[node]:
                if distance[adjacent_node] > distance[node] + graph[node][adjacent_node][weight] and distance[node] != float('Inf'):
                    distance[adjacent_node] = distance[node] + graph[node][adjacent_node][weight]
                    pred[adjacent_node] = node
    path = []
    node = end
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0,node)
            node = pred[node]
        else:
            break
    path.insert(0, start)   
    return {'path': path, 'length': distance[end]}
