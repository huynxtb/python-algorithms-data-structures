# Kosaraju's Algorithm for Strongly Connected Components (SCCs)

## 1. Introduction
Kosaraju's algorithm is a linear-time algorithm used to find the Strongly Connected Components (SCCs) of a directed graph. A strongly connected component is a maximal subgraph where every vertex is reachable from every other vertex in the same subgraph. This algorithm is highly useful in social network analysis, cycle detection, and resolving dependencies in package managers.

## 2. Usage

from kosaraju_scc import KosarajuSCC

# Initialize a graph with 5 vertices (0 to 4)
graph = KosarajuSCC(5)

# Add directed edges
graph.add_edge(1, 0)
graph.add_edge(0, 2)
graph.add_edge(2, 1)
graph.add_edge(0, 3)
graph.add_edge(3, 4)

# Find Strongly Connected Components
sccs = graph.find_sccs()
print(sccs)  # Output: [[3], [4], [0, 1, 2]] (order of components and vertices may vary)


## 3. Detailed Explanation
Kosaraju's algorithm operates in three main phases:
1. **First DFS Pass (Ordering)**: Perform a Depth First Search (DFS) on the original graph. As vertices finish processing (i.e., all their neighbors have been visited), push them onto a stack. This orders vertices by their finishing times.
2. **Graph Transposition**: Create a transposed copy of the graph where the direction of every edge is reversed.
3. **Second DFS Pass (Collection)**: Pop vertices from the stack one by one. If a vertex has not been visited, perform a DFS on the transposed graph starting from this vertex. All vertices reached during this DFS form a single Strongly Connected Component.

## 4. Complexity Analysis
- **Time Complexity**: $O(V + E)$, where $V$ is the number of vertices and $E$ is the number of edges. The algorithm performs two complete DFS traversals and one graph transposition, each taking linear time.
- **Space Complexity**: $O(V + E)$ to store the adjacency list of the original graph, the transposed graph, the recursion stack, and the tracking structures.