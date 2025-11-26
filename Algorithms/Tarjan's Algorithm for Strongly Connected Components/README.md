# Tarjan's Algorithm for Strongly Connected Components (SCC)

## Introduction
Tarjan's Algorithm is a classical method used to find all strongly connected components (SCCs) in a directed graph. A strongly connected component is defined as a maximal subset of vertices such that every vertex in the subset is reachable from every other vertex in the same subset. This algorithm is efficient and runs in linear time relative to the number of graph edges and vertices.

Use it when you need to identify clusters of nodes that are mutually reachable, which is a common requirement in applications such as program analysis, graph partitioning, and network connectivity problems.

---

## Usage
Below is an example of how to use the provided `TarjanSCC` class in Python:

Create an instance of the TarjanSCC class
scc_finder = TarjanSCC()

Define a directed graph as an adjacency list (dictionary)
graph = {
    'A': ['B'],
    'B': ['C', 'E', 'F'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['A', 'F'],
    'F': ['G'],
    'G': ['F'],
    'H': ['D', 'G']
}

Find strongly connected components
components = scc_finder.strongly_connected_components(graph)

components will be a list of SCCs, e.g., [['C', 'D', 'H'], ['F', 'G'], ['A', 'B', 'E']]

---

## Detailed Explanation

- The class `TarjanSCC` encapsulates the Tarjan's algorithm.
- `strongly_connected_components(graph)` is the public method that takes an adjacency list representation of a graph.
- It initializes bookkeeping structures and iterates over all nodes.
- `_strongconnect(node, graph)` is a recursive helper method that:
  - Assigns each node an index (discovery time) and a low-link value.
  - Uses a stack to keep track of the current path of nodes being explored.
  - Updates the low-link values by visiting neighbors.
  - Identifies when a strongly connected component is found (when the node's low-link equals its index), at which point it pops nodes off the stack to form an SCC.

This method ensures each node and edge is processed exactly once, guaranteeing efficiency.

---

## Complexity Analysis

- **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges in the graph. Each node and edge is visited once.

- **Space Complexity:** O(V), due to storage for the recursion stack, bookkeeping dictionaries, and the stack used to track nodes.

The implementation uses dictionaries and sets for efficient lookup and state management, making it both clear and performant.

---

This class can be directly reused or extended in larger graph processing systems or research software requiring SCC computation.