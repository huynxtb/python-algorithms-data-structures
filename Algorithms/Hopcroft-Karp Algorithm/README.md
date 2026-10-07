# Hopcroft-Karp Algorithm

## 1. Introduction
The **Hopcroft-Karp Algorithm** is an efficient algorithm that finds a Maximum Cardinality Matching in an unweighted bipartite graph $G = (U, V, E)$. 

A matching in a graph is a set of edges without common vertices. A maximum cardinality matching contains the largest possible number of edges. Hopcroft-Karp is especially useful in assignment problems, task allocation, network flow applications, and bipartite graph modeling where performance faster than the standard augmenting path approach (such as Ford-Fulkerson or Kuhn's Algorithm) is required.

## 2. Usage


from HopcroftKarp import HopcroftKarp

# Define bipartite graph partitions
left_partition = {"U1", "U2", "U3", "U4"}
right_partition = {"V1", "V2", "V3", "V4"}

# Define adjacency list from left partition to right partition
edges = {
    "U1": {"V1", "V2"},
    "U2": {"V1", "V3"},
    "U3": {"V2", "V4"},
    "U4": {"V3", "V4"},
}

# Instantiate and compute maximum matching
solver = HopcroftKarp(left_partition, right_partition, edges)
matching = solver.max_matching()

# Result:
# {'U1': 'V2', 'U2': 'V1', 'U3': 'V4', 'U4': 'V3'} (or another valid maximum matching of size 4)
print(matching)


## 3. Detailed Explanation
The Hopcroft-Karp algorithm improves upon the $O(V \cdot E)$ Ford-Fulkerson / augmenting path approach by finding a **maximal set of shortest vertex-disjoint augmenting paths** in each phase.

Each phase consists of two steps:
1. **Breadth-First Search (BFS)**:
   - Starts simultaneously from all unmatched vertices in the left partition ($U$).
   - Traverses alternating edges (unmatched edges from $U$ to $V$, matched edges from $V$ to $U$).
   - Assigns distance levels to vertices in $U$ and identifies the length of the shortest augmenting path that reaches an unmatched vertex in $V$ (represented via the sentinel dummy vertex `_NIL`).
2. **Depth-First Search (DFS)**:
   - Traverses only along the forward edges of the shortest-path layered graph ($dist[next] = dist[curr] + 1$).
   - Finds vertex-disjoint augmenting paths and updates the matching along each path immediately.
   - Marks dead-end paths ($dist[u] = \infty$) to eliminate redundant searches within the same phase.

This process terminates when BFS can no longer find any augmenting paths.

## 4. Complexity Analysis
- **Time Complexity**:
  - **Per Phase**: $\mathcal{O}(|V| + |E|)$ as each vertex and edge is examined a constant number of times during BFS and DFS.
  - **Number of Phases**: At most $\mathcal{O}(\sqrt{|V|})$, because the shortest augmenting path length strictly increases each phase, and after $\sqrt{|V|}$ phases, the remaining maximum matching can only be augmented at most $\mathcal{O}(\sqrt{|V|})$ times.
  - **Total Time Complexity**: $\mathcal{O}(|E| \sqrt{|V|})$, where $|V| = |U| + |V|$.
- **Space Complexity**:
  - $\mathcal{O}(|V| + |E|)$ auxiliary space to store partition sets, adjacency lists, distance arrays, and matching pointers.
