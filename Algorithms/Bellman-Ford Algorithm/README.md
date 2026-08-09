# Bellman-Ford Algorithm

## 1. Introduction
The Bellman-Ford algorithm computes shortest paths from a single source vertex to all other vertices in a weighted digraph. Unlike Dijkstra's algorithm, Bellman-Ford supports graphs containing negative edge weights and can detect negative-weight cycles reachable from the source.

## 2. Usage

from bellman_ford import bellman_ford, NegativeCycleError

# Graph with 5 vertices (0 to 4)
edges = [
    (0, 1, -1.0),
    (0, 2, 4.0),
    (1, 2, 3.0),
    (1, 3, 2.0),
    (1, 4, 2.0),
    (3, 2, 5.0),
    (3, 1, 1.0),
    (4, 3, -3.0)
]

try:
    distances, predecessors = bellman_ford(vertices_count=5, edges=edges, source=0)
    print("Distances:", distances)
    print("Predecessors:", predecessors)
except NegativeCycleError as e:
    print(e)


## 3. Detailed Explanation
The algorithm initializes the distance to the source vertex to `0` and all other vertices to infinity (`inf`). It then repeatedly relaxes all edges $|V| - 1$ times, where $|V|$ is the number of vertices. In each iteration, it updates the shortest distance to a destination vertex if a shorter path is found through a source vertex. An early termination optimization stops the loop if no distances are updated during an iteration. Finally, it performs one more pass over all edges to check for negative-weight cycles. If a distance can still be minimized, a negative-weight cycle exists, and the algorithm raises a `NegativeCycleError`.

## 4. Complexity Analysis
- **Time Complexity**:
  - Worst-case: $O(V \cdot E)$ where $V$ is the number of vertices and $E$ is the number of edges.
  - Best-case: $O(E)$ when no updates occur after the first iteration.
- **Space Complexity**: $O(V)$ to store the distances and predecessors dictionaries.