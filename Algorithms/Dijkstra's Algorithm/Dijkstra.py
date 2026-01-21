import heapq
from typing import Dict, List, Tuple, Any

class Dijkstra:
    @staticmethod
    def shortest_paths(graph: Dict[Any, List[Tuple[Any, float]]], start: Any) -> Dict[Any, float]:
        """
        Calculate the shortest distance from start node to all other nodes in the graph using Dijkstra's Algorithm.

        Args:
            graph (Dict[Any, List[Tuple[Any, float]]]): The weighted graph represented as an adjacency list.
                Each key is a node, and the value is a list of tuples (neighbor, weight).
            start (Any): The starting node for shortest paths calculation.

        Returns:
            Dict[Any, float]: A dictionary mapping each node to its shortest distance from start.
                              Nodes unreachable from start will have distance float('inf').
        """
        distances = {node: float('inf') for node in graph}
        distances[start] = 0.0
        priority_queue = [(0.0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph.get(current_node, []):
                if weight < 0:
                    continue
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
