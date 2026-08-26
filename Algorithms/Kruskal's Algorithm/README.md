# Kruskal's Algorithm

## 1. Introduction
Kruskal's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph. An MST is a subset of the edges that connects all vertices together without any cycles and with the minimum possible total edge weight. This algorithm is widely used in network design (e.g., telephone, electrical, computer networks) and approximation algorithms for traveling salesperson problems.

## 2. Usage

from kruskals_mst import KruskalMST

# Define graph parameters
num_vertices = 4
edges = [
    (0, 1, 10.0),
    (0, 2, 6.0),
    (0, 3, 5.0),
    (1, 3, 15.0),
    (2, 3, 4.0)
]

try:
    mst, total_weight = KruskalMST.find_mst(num_vertices, edges)
    print("MST Edges:", mst)
    print("Total Weight:", total_weight)
except ValueError as e:
    print("Error:", e)


## 3. Detailed Explanation
The algorithm operates as follows:
1. **Sort Edges**: Sort all the graph edges in non-decreasing order of their weight.
2. **Initialize Disjoint Set**: Create a Disjoint Set (Union-Find) data structure where each vertex is initially in its own set.
3. **Iterate and Union**: Iterate through the sorted edges. For each edge `(u, v)`:
   - Check if `u` and `v` belong to different sets using the `find` operation.
   - If they are in different sets, adding the edge will not form a cycle. Add the edge to the MST and merge the sets containing `u` and `v` using the `union` operation.
   - If they are in the same set, discard the edge to avoid forming a cycle.
4. **Termination**: Stop when the MST contains `num_vertices - 1` edges. If the loop finishes and we have fewer than `num_vertices - 1` edges, the graph is disconnected, and a single MST cannot be formed.

To optimize performance, the `DisjointSet` class implements:
- **Path Compression**: Flattens the structure of the tree during `find` operations, making future lookups faster.
- **Union by Rank**: Attaches the smaller depth tree under the root of the deeper tree during `union` operations, keeping the tree balanced.

## 4. Complexity Analysis
- **Time Complexity**:
  - **Sorting Edges**: $O(E \log E)$, where $E$ is the number of edges.
  - **Union-Find Operations**: $O(E \cdot \alpha(V))$, where $V$ is the number of vertices and $\alpha$ is the Inverse Ackermann function (which grows extremely slowly and is practically constant).
  - **Total Time Complexity**: $O(E \log E)$ or $O(E \log V)$ since $E \le V^2$ and $\log E \le 2 \log V$.
- **Space Complexity**: $O(V)$ to store the parent and rank arrays in the `DisjointSet` data structure.
