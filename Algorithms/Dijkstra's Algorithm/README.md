# Dijkstra's Algorithm

## 1. Introduction

Dijkstra's Algorithm is a classical algorithm used to find the shortest paths from a single source node to all other nodes in a weighted graph with non-negative edge weights. It is widely applied in network routing protocols, mapping software, and any systems requiring shortest path calculations on graphs.

This implementation uses a priority queue (min-heap) and adjacency list representation of graphs to provide an efficient, reusable solution suitable for integration in larger Python projects.

## 2. Usage

The `Dijkstra` class provides a static method `shortest_paths` that calculates shortest distances from a start node to every other node. The graph should be represented as a dictionary where each key is a node and the value is a list of tuples representing neighbors and edge weights.

Example usage:

from Dijkstra import Dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
distances = Dijkstra.shortest_paths(graph, start_node)
print(distances)

Expected Output:
{'A': 0.0, 'B': 1.0, 'C': 3.0, 'D': 4.0}

## 3. Details

- Graph is represented as adjacency list: {node: [(neighbor, weight), ...]}
- Uses min-heap queue for efficient closest node retrieval
- Skips processing if non-optimal path is found
- Supports disconnected nodes (distance remains infinity)

## 4. Complexity

- Time: O(E log V), E edges and V vertices
- Space: O(V + E) for graph, plus O(V) for distances and queue

