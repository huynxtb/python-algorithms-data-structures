class FloydWarshall:
    @staticmethod
    def shortest_paths(graph):
        """
        Compute the shortest paths between all pairs of vertices in a weighted graph using the Floyd-Warshall algorithm.

        Parameters:
        graph (list of list of float): A 2D adjacency matrix representing the graph where graph[i][j] is the weight from vertex i to j,
                                     and a large sentinel value (like float('inf')) if no direct edge exists.

        Returns:
        list of list of float: A matrix with the shortest distances between every pair of vertices.
        """
        # Number of vertices
        n = len(graph)

        # Initialize distance matrix with graph values
        dist = [row[:] for row in graph]  # deep copy

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If vertex k is on the shortest path from i to j, update the dist[i][j]
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist
