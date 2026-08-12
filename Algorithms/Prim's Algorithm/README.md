# Prim's Algorithm

### 1. Introduction
Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a weighted, undirected graph. An MST is a subset of the edges that connects all vertices together without any cycles and with the minimum possible total edge weight. This algorithm is highly efficient for dense graphs and is widely used in network design, routing, and clustering.

### 2. Usage

from prims_algorithm import PrimsAlgorithm

# Define an undirected graph as an adjacency list
graph = {
    0: [(1, 4.0), (2, 3.0)],
    1: [(0, 4.0), (2, 1.0), (3, 2.0)],
    2: [(0, 3.0), (1, 1.0), (3, 5.0)],
    3: [(1, 2.0), (2, 5.0)]
}

prim = PrimsAlgorithm()
edges, total_weight = prim.find_mst(graph, start_node=0)

print("MST Edges:", edges)
print("Total Weight:", total_weight)


### 3. Detailed Explanation
The implementation utilizes a min-heap to greedily select the minimum weight edge connecting a visited vertex to an unvisited vertex.
1. **Validation**: The algorithm first checks if the `start_node` exists in the graph. If not, it raises a `ValueError`.
2. **Initialization**: A `visited` set is initialized with the `start_node`. All outgoing edges from the `start_node` are pushed onto the min-heap.
3. **Main Loop**: The algorithm repeatedly pops the minimum weight edge `(weight, u, v)` from the heap. If the destination node `v` is already visited, the edge is discarded. Otherwise, `v` is marked as visited, the edge is added to the MST, and all outgoing edges from `v` to unvisited neighbors are pushed onto the heap.
4. **Connectivity Check**: Once the heap is empty or all nodes are visited, the algorithm checks if the number of visited nodes equals the total number of nodes in the graph. If they do not match, a `ValueError` is raised indicating the graph is disconnected.

### 4. Complexity Analysis
- **Time Complexity**: $O(E \log V)$ where $E$ is the number of edges and $V$ is the number of vertices. Each edge is pushed and popped from the priority queue at most once, taking $O(\log E)$ time, which simplifies to $O(\log V)$ since $E \le V^2$.
- **Space Complexity**: $O(V + E)$ to store the visited set, the priority queue, and the resulting MST edges.