# Breadth First Search (BFS)

## Introduction

Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores nodes level by level starting from a specified source vertex. It is commonly used to traverse or search graphs and trees. BFS visits all nodes at the present depth before moving on to nodes at the next depth level. This algorithm is particularly useful for finding the shortest path on unweighted graphs, exploring connectivity, and many other real-world graph-based problems.

## Usage

To use the BFS implementation, you call the static method `traverse` of the BFS class. You pass in a graph represented as a dictionary (adjacency list) and a starting node. The function returns a list of nodes in the order they are visited.

Example usage:

    # Define the graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Perform BFS starting from node 'A'
    visited_order = BFS.traverse(graph, 'A')
    print(visited_order)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']

## Detailed Explanation

- The graph is represented as an adjacency list using a dictionary where each key is a node and the value is a list of adjacent nodes.
- BFS is implemented as a static method `traverse` inside the `BFS` class.
- A queue (deque) is used to process nodes in a FIFO manner.
- A set keeps track of visited nodes to prevent visiting the same node multiple times.

Steps of the algorithm:
1. Initialize a queue and add the start node to it.
2. Mark the start node as visited.
3. While the queue is not empty:
   - Dequeue the node from the front of the queue.
   - Add this node to the traversal order list.
   - Enqueue all unvisited neighbors of this node and mark them as visited.

This ensures nodes are explored level by level from the start node. The BFS traversal order reflects the order nodes are reached in layers from the start.

Nodes disconnected from the start node are not visited.

## Complexity Analysis

- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. Each node and edge is processed at most once.
- Space Complexity: O(V), due to the queue and the set to track visited nodes.

This makes BFS efficient for traversal on sparse and dense graphs represented with adjacency lists.
