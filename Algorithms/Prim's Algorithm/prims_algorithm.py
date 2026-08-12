import heapq

class PrimsAlgorithm:
    """
    An implementation of Prim's Algorithm to find the Minimum Spanning Tree (MST)
    of a weighted, undirected graph.
    """

    def find_mst(
        self, graph: dict[int, list[tuple[int, float]]], start_node: int
    ) -> tuple[list[tuple[int, int, float]], float]:
        """
        Finds the Minimum Spanning Tree (MST) of a weighted, undirected graph starting from a given node.

        Args:
            graph: Adjacency list representing the graph. Keys are node IDs,
                   values are lists of tuples (neighbor, weight).
            start_node: The node ID to start the MST construction.

        Returns:
            A tuple containing:
                - A list of edges in the MST, where each edge is (node_u, node_v, weight).
                - The total weight of the MST.

        Raises:
            ValueError: If the start_node is not in the graph, or if the graph is disconnected.
        """
        if start_node not in graph:
            raise ValueError("Start node is not present in the graph.")

        visited = {start_node}
        mst_edges = []
        total_weight = 0.0
        min_heap = []

        # Push all initial edges from the start node into the priority queue
        for neighbor, weight in graph[start_node]:
            heapq.heappush(min_heap, (weight, start_node, neighbor))

        num_nodes = len(graph)

        while min_heap and len(visited) < num_nodes:
            weight, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight

            for neighbor, next_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, neighbor))

        if len(visited) != num_nodes:
            raise ValueError("The graph is disconnected; a single spanning tree cannot be formed.")

        return mst_edges, total_weight
