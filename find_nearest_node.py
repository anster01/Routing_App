from sklearn.neighbors import KDTree
import pandas as pd

def NearestNode(coords, node_pos):
    nodes = pd.DataFrame.from_dict(node_pos, orient='index', columns=['y','x'])
    tree = KDTree(nodes[['x','y']], metric='euclidean')
    nearest_nodes = []
    for location in coords:
        idx = tree.query([location], k=1, return_distance=False)[0]
        nearest_nodes.append(nodes.iloc[idx].index.values[0])
    return nearest_nodes
