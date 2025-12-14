# Breadth-First Search (BFS) Algorithm

## Introduction
Breadth-First Search (BFS) is a fundamental graph traversal algorithm used to explore nodes in a graph level by level. It starts from a given source node and explores all neighbors at the present depth prior to moving on to nodes at the next depth level. BFS works on both directed and undirected graphs and can be used for shortest path search in unweighted graphs, detecting connectivity, and level-order traversal.

## Usage
Here's how to use the BFS implementation provided:

    # Initialize a graph with an adjacency list
    adjacency = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    graph = Graph(adjacency)

    # Perform BFS starting from node 'A'
    order = graph.bfs('A')
    print(order)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']

## Detailed Explanation
The `Graph` class contains an adjacency list representation of the graph where each key is a node and the value is a list of its neighboring nodes.

The BFS method works as follows:
1. Initialize a queue and add the start node to it.
2. Use a set `visited` to keep track of nodes that have already been explored.
3. Dequeue a node, mark it visited, and add it to the order list.
4. Enqueue all unvisited neighbors of the dequeued node.
5. Repeat until the queue is empty.

This ensures nodes are visited in order of their distance from the start node, i.e., level by level.

## Complexity Analysis
- **Time Complexity:** O(V + E) where V is the number of vertices and E is the number of edges. Each vertex and edge is visited at most once.
- **Space Complexity:** O(V) in the worst case for storing the queue, visited set, and the order list, where V is the number of vertices.

This implementation does not handle input validation or graph mutation. It aims to be a straightforward reusable BFS module for integration in larger projects.