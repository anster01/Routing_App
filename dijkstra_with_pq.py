from priority_queue import Priority_Queue

def dijkstra_with_pq(graph, start, end, weight):
    distance = {}
    pred = {}

    for node in graph.keys():
        distance[node] = float('Inf')
        pred[node] = ''
    distance[start] = 0
    priority_queue = Priority_Queue()
    priority_queue.push([distance[start], start])

    while priority_queue.elements:
        node_value, node = priority_queue.pop()
        if node_value == distance[node]:
            for adjacent_node, adjacent_value in graph[node].items():
                if distance[node] + adjacent_value[weight] < distance[adjacent_node]:
                    distance[adjacent_node] = distance[node] + adjacent_value[weight]
                    priority_queue.push([distance[adjacent_node], adjacent_node])
                    pred[adjacent_node] = node
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
