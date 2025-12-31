# Topological Sort using DFS

## 1. Introduction
Topological Sort is an algorithm for ordering the vertices of a Directed Acyclic Graph (DAG) such that for every directed edge u -> v, vertex u comes before vertex v in the ordering. It is widely used to schedule tasks, resolve dependencies, and order computations where certain prerequisites must be met before proceeding.

This implementation uses Depth-First Search (DFS) to produce a valid topological order when given a DAG. It also detects cycles in the graph and raises an exception if any are found, as topological ordering is undefined for graphs with cycles.

## 2. Usage

# Create a graph
graph = DirectedGraph()

# Add edges (u -> v)
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

# Compute topological sort
try:
    order = graph.topological_sort()
    print(order)  # Example output: ['B', 'A', 'C', 'D', 'E']
except GraphCycleError as e:
    print(f"Cycle detected: {e}")

## 3. Detailed Explanation
- The `DirectedGraph` class uses an adjacency list to store graph edges. Vertices are keys in a dictionary, and each vertex maps to a set of adjacent vertices.
- The `add_vertex` method adds a vertex if it does not exist.
- The `add_edge` method adds directed edges and implicitly adds vertices if they are missing.
- The `topological_sort` method performs DFS on each unvisited vertex. It tracks the visitation state of each vertex:
  - "unvisited": not visited yet
  - "visiting": currently explored (helps detect cycles)
  - "visited": exploration completed
- When a vertex is first visited, state changes from "unvisited" to "visiting".
- The algorithm recursively visits neighbors. If we visit a vertex already in "visiting" state, it indicates a cycle, so `GraphCycleError` is raised.
- After visiting a vertex's neighbors, it is marked as "visited" and appended to the list.
- The final topological order is the reverse of the order vertices are completed.

## 4. Complexity Analysis
- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. Each vertex and edge is explored once in DFS.
- Space Complexity: O(V + E) for storing the graph and recursion stack; O(V) for the state tracking and output list.

This implementation provides a clean, reusable Python class encapsulating the graph and topological sorting functionality, complete with cycle detection for robustness.
