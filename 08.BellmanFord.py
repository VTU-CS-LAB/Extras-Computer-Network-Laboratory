import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt
import sys

def bellmanFord(adj, dest):
    n = len(adj)
    distanceVector = [sys.maxint for i in range(n)]
    distanceVector[dest_vertex - 1] = 0
    for i in range(n - 1):
        prevDistanceVector = distanceVector
        for j in range(n):
            min = sys.maxint
            for k in range(n):
                if min > adj[j, k] + prevDistanceVector[k]:
                    min = adj[j, k] + prevDistanceVector[k]
            distanceVector[j] = min
    return distanceVector

if __name__ == '__main__':
    n = 7
    #using math.inf for infinity values
    G = nx.gnm_random_graph(n, 4, seed = 5768465)
    adjMatrix = nx.to_numpy_matrix(G)
    #randomizing values in graph to make it more realistic
    mask = np.random.randint(0,2,size=adjMatrix.shape).astype(np.bool)
    temp = np.random.rand(*adjMatrix.shape) * np.max(G)
    adjMatrix[mask] = temp[mask]
    adjMatrix += 1
    print(adjMatrix)
    np.fill_diagonal(adjMatrix, 0)
    G = nx.from_numpy_matrix(adjMatrix)
    G.add_weighted_edges_from((u, v, adjMatrix[u, v]) for u, v in G.edges())
    nx.draw(G)
    plt.show()
    #graph visualised.
    # print(adjMatrix)
    dest_vertex = 3
    solution = bellmanFord(adjMatrix, dest_vertex)
    print("Solution Vector:")
    print(list(solution))
