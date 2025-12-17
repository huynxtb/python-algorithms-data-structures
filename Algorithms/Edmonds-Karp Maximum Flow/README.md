# Edmonds-Karp Maximum Flow Algorithm

## Introduction
Edmonds-Karp is an implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network. It uses Breadth-First Search (BFS) to find augmenting paths, which ensures the shortest path in terms of number of edges is used in every augmentation step. This guarantees polynomial time complexity.

This algorithm is fundamental in network flow analysis and is widely used in problems involving maximum bipartite matching, network routing, and resource allocation.

## Usage
Here's how to use the `MaxFlowEdmondsKarp` class:

max_flow_solver = MaxFlowEdmondsKarp(6)
max_flow_solver.add_edge(0, 1, 16)
max_flow_solver.add_edge(0, 2, 13)
max_flow_solver.add_edge(1, 2, 10)
max_flow_solver.add_edge(2, 1, 4)
max_flow_solver.add_edge(1, 3, 12)
max_flow_solver.add_edge(3, 2, 9)
max_flow_solver.add_edge(2, 4, 14)
max_flow_solver.add_edge(4, 3, 7)
max_flow_solver.add_edge(3, 5, 20)
max_flow_solver.add_edge(4, 5, 4)
max_flow = max_flow_solver.max_flow(0, 5)
print(f"Maximum flow: {max_flow}")

## Detailed Explanation
The implementation represents the flow network as adjacency lists storing forward and backward edges. Each edge is stored with a capacity and a reverse index for easy residual graph updates.

### Key methods:
- `add_edge(frm, to, capacity)`: Adds forward and residual backward edges.
- `bfs(source, sink, parent)`: Performs BFS to find an augmenting path.
- `max_flow(source, sink)`: Repeatedly uses BFS to find augmenting paths until no more exist.

When BFS finds a path, it determines the bottleneck capacity along the path and updates the capacities of the edges along that path (reducing forward edge capacities and increasing back edges). This process repeats until no augmenting path exists.

## Complexity Analysis
- Time Complexity: O(V * E^2), where V is the number of vertices and E is the number of edges. This comes from BFS taking O(E) time and potentially O(V*E) augmentations.
- Space Complexity: O(V + E) due to storing the graph in adjacency lists.

This implementation is suitable for medium-sized networks. For larger networks, more advanced algorithms like Dinic's or Push-Relabel may perform better.