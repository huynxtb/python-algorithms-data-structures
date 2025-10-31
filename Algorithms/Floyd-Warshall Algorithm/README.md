# Floyd-Warshall Algorithm

## 1. Introduction

The Floyd-Warshall Algorithm is a classic dynamic programming algorithm used to find the shortest paths between all pairs of vertices in a weighted graph. Unlike algorithms like Dijkstra's, which find the shortest path from a single source to all other vertices, Floyd-Warshall handles every pair of nodes simultaneously. It can handle graphs with positive and negative edge weights, but there must be no negative weight cycles.

Use this algorithm when you need the shortest distance between every pair of nodes in a graph efficiently and wish to handle graphs with negative edges (but no negative cycles).

---

## 2. Usage

Below is a simple usage example for the provided `FloydWarshall` class:

INF = float('inf')

# Example adjacency matrix of a graph
# graph[i][j] = weight from vertex i to j
# INF means no direct edge
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Compute shortest paths:
shortest_distances = FloydWarshall.shortest_paths(graph)

# shortest_distances will now be a matrix representing the shortest paths between all pairs

---

## 3. Detailed Explanation

The algorithm works by iteratively improving the estimate of the shortest path between every pair of vertices. Initially, the distance from vertex `i` to vertex `j` is set to the weight of the direct edge, or infinity if no direct edge exists. Then for each vertex `k`, the algorithm checks if the path from `i` to `j` can be shortened by going through `k`. If so, it updates the distance.

Formally:

Let `dist[i][j]` be the shortest known distance from vertex `i` to vertex `j` after considering vertices from the set {1,...,k}. For k from 1 to n:

    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

This dynamic programming relation ensures that by the end, all shortest paths considering any intermediate nodes are accounted for.

---

## 4. Complexity Analysis

- Time Complexity: O(n^3), where n is the number of vertices. The triple nested loops arise from considering every pair (i, j) for every intermediate node k.
- Space Complexity: O(n^2) for storing the distance matrix.

While the time complexity is cubic, this algorithm is efficient and often the most straightforward choice when you need shortest paths for all pairs in dense graphs or graphs with negative edge weights but no negative cycles.
