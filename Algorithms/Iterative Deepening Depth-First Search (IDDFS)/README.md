# Iterative Deepening Depth-First Search (IDDFS)

## Introduction

Iterative Deepening Depth-First Search (IDDFS) is a graph traversal algorithm that combines the space efficiency of Depth-First Search (DFS) with the completeness and optimality (for unweighted graphs) of Breadth-First Search (BFS). Unlike standard DFS which can get stuck exploring deep paths, IDDFS performs a series of depth-limited DFS searches with incrementally increasing depth limits (0, 1, 2, 3, ...) until the target is found or the entire graph is exhausted.

IDDFS is particularly useful when:
- You need to find the shortest path in an unweighted graph
- Memory is constrained and BFS would use too much space
- The search space is large and you want to avoid exploring unnecessary depths
- You want guaranteed completeness without storing all nodes in memory like BFS does

## Usage


from iddfs import Graph, iddfs, iddfs_all_paths

# Create a graph
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("D", "G")

# Find a path using IDDFS
found, path, depth = iddfs(graph, "A", "G", max_depth=5)
print(f"Found: {found}, Path: {path}, Depth: {depth}")
# Output: Found: True, Path: ['A', 'B', 'D', 'G'], Depth: 3

# Find all shortest paths
paths, depth = iddfs_all_paths(graph, "A", "D", max_depth=5)
print(f"All shortest paths: {paths}, Depth: {depth}")
# Output: All shortest paths: [['A', 'B', 'D']], Depth: 2

# Edge case: source equals target
found, path, depth = iddfs(graph, "A", "A", max_depth=5)
print(f"Source == Target: Found: {found}, Path: {path}, Depth: {depth}")
# Output: Source == Target: Found: True, Path: ['A'], Depth: 0


## Detailed Explanation

### Graph Representation
The implementation uses an adjacency list to represent the graph. Each node maps to a list of its neighbors, allowing efficient neighbor lookups.

### Depth-Limited Search (DLS)
The `depth_limited_search` function implements recursive DFS with a depth constraint:
1. It maintains a visited set to avoid cycles
2. At each node, it checks if the target has been reached
3. If the current depth reaches 0, it backtracks
4. For each unvisited neighbor, it recursively explores to depth-1
5. Returns immediately upon finding the target

### Iterative Deepening
The `iddfs` function repeatedly calls `depth_limited_search` with increasing depth limits:
1. Starts with depth limit 0, then 1, 2, 3, and so on
2. Each iteration performs a complete DLS from the source
3. Returns immediately when the target is found, along with the depth at which it was found
4. This approach guarantees finding the shortest path in unweighted graphs

### Finding All Shortest Paths
The `iddfs_all_paths` function extends IDDFS to find all shortest paths:
1. For each depth limit, it finds all paths within that depth
2. Uses backtracking with a visited set that's managed locally per branch
3. Returns all paths found at the minimum depth where at least one path exists
4. This gives all optimal solutions rather than just one

### Edge Case Handling
- If source equals target, returns immediately with depth 0
- If source is not in the graph, returns not found
- Disconnected nodes are handled naturally (search terminates without finding target)
- The algorithm is complete: it will find a solution if one exists

## Complexity Analysis

### Time Complexity
- **IDDFS Single Path**: O(b^d) where b is the branching factor and d is the depth of the solution
  - Although we revisit nodes multiple times (once per depth level from 0 to d), each depth level k explores at most O(b^k) nodes
  - Total: O(b^0 + b^1 + b^2 + ... + b^d) = O(b^d)
  - This is the same as a single DFS to depth d

- **IDDFS All Paths**: O(b^d × p) where p is the number of shortest paths
  - Finding all paths requires exploring all branches, but only up to depth d

### Space Complexity
- **IDDFS Single Path**: O(d) where d is the depth of the solution
  - Uses a recursion stack of depth d and a visited set containing at most d nodes per branch
  - This is significantly better than BFS which uses O(b^d) space

- **IDDFS All Paths**: O(d × p) where p is the number of shortest paths
  - Must store all paths found, each of length d

### Why IDDFS is Optimal
While IDDFS revisits nodes multiple times, the total work is still O(b^d) because:
- Depth 0: explores 1 node
- Depth 1: explores b nodes
- Depth 2: explores b^2 nodes
- The sum forms a geometric series dominated by the largest term b^d

This makes IDDFS ideal when you need BFS guarantees (shortest path, completeness) but DFS memory efficiency.
