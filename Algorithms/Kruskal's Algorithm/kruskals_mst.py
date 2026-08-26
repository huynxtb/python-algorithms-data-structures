class DisjointSet:
    """Representation of a Disjoint Set (Union-Find) data structure with path compression and union by rank."""

    def __init__(self, size: int) -> None:
        """Initializes the disjoint set with 'size' elements."""
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i: int) -> int:
        """Finds the representative of the set containing element i, applying path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """Unites the sets containing elements i and j. Returns True if united, False if already in the same set."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


class KruskalMST:
    """Kruskal's Algorithm implementation to find the Minimum Spanning Tree (MST)."""

    @staticmethod
    def find_mst(
        num_vertices: int,
        edges: list[tuple[int, int, float]]
    ) -> tuple[list[tuple[int, int, float]], float]:
        """
        Finds the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph.

        Args:
            num_vertices: The number of vertices in the graph (vertices indexed 0 to num_vertices - 1).
            edges: A list of tuples representing undirected edges (u, v, weight).

        Returns: 
            A tuple containing:
            - A list of edges included in the MST.
            - The total weight of the MST.

        Raises:
            ValueError: If the graph is disconnected, num_vertices is invalid, or input is empty.
        """
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be greater than 0.")
        if num_vertices == 1:
            return [], 0.0

        # Sort edges by weight
        sorted_edges = sorted(edges, key=lambda edge: edge[2])
        
        ds = DisjointSet(num_vertices)
        mst_edges: list[tuple[int, int, float]] = []
        total_weight = 0.0
        edges_count = 0

        for u, v, weight in sorted_edges:
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                raise ValueError(f"Vertex index out of bounds: {u} or {v}")
            if ds.union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                edges_count += 1
                if edges_count == num_vertices - 1:
                    break

        if edges_count < num_vertices - 1:
            raise ValueError("The graph is disconnected; a single minimum spanning tree cannot be formed.")

        return mst_edges, total_weight
