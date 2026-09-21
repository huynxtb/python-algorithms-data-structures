class BipartiteMatching:
    """
    Implements the Ford-Fulkerson algorithm to find the maximum cardinality
    bipartite matching using augmenting paths found via Depth-First Search (DFS).
    """

    def __init__(self, num_left: int, num_right: int):
        """
        Initializes the BipartiteMatching object.

        Args:
            num_left: The number of vertices in the left partition (U).
            num_right: The number of vertices in the right partition (V).
        """
        self.num_left = num_left
        self.num_right = num_right
        self.adj = [[] for _ in range(num_left)]

    def add_edge(self, u: int, v: int) -> None:
        """
        Adds a directed edge from a vertex in the left partition to a vertex
        in the right partition.

        Args:
            u: The index of the vertex in the left partition (0-indexed).
            v: The index of the vertex in the right partition (0-indexed).
        """
        if not (0 <= u < self.num_left):
            raise ValueError(f"Vertex u ({u}) out of bounds for left partition [0, {self.num_left-1}]")
        if not (0 <= v < self.num_right):
            raise ValueError(f"Vertex v ({v}) out of bounds for right partition [0, {self.num_right-1}]")
        self.adj[u].append(v)

    def _dfs(self, u: int, visited: list[bool], match_right: list[int]) -> bool:
        """
        Helper function to find an augmenting path from vertex u using DFS.

        Args:
            u: The current vertex in the left partition.
            visited: A list of booleans indicating if a right vertex has been visited
                     in the current DFS traversal.
            match_right: A list where match_right[v] stores the left vertex matched
                         with right vertex v, or -1 if v is unmatched.

        Returns:
            True if an augmenting path is found, False otherwise.
        """
        for v in self.adj[u]:
            if not visited[v]:
                visited[v] = True
                # If vertex v is not matched, or if it is matched and the
                # matched vertex can find an alternative path, then match u with v.
                if match_right[v] == -1 or self._dfs(match_right[v], visited, match_right):
                    match_right[v] = u
                    return True
        return False

    def max_matching(self) -> tuple[int, list[tuple[int, int]]]:
        """
        Computes the maximum cardinality bipartite matching.

        Returns:
            A tuple containing:
            - The size of the maximum matching (int).
            - A list of matched edges, where each edge is a tuple (u, v)
              representing a match between left vertex u and right vertex v.
        """
        # Initialize matching for right partition vertices. -1 indicates no match.
        match_right = [-1] * self.num_right
        matching_size = 0

        # Iterate through all vertices in the left partition
        for u in range(self.num_left):
            # Mark all right vertices as not visited for the current DFS traversal
            visited = [False] * self.num_right
            # If an augmenting path is found starting from u, increment matching size
            if self._dfs(u, visited, match_right):
                matching_size += 1

        # Construct the list of matched edges
        matches = []
        for v in range(self.num_right):
            if match_right[v] != -1:
                matches.append((match_right[v], v))

        return matching_size, matches
