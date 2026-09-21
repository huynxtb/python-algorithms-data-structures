# Bipartite Matching (Ford-Fulkerson with DFS)

## Introduction

The Bipartite Matching algorithm, specifically implemented here using the Ford-Fulkerson method with Depth-First Search (DFS) for finding augmenting paths, is used to find the maximum number of edges that can be selected in a bipartite graph such that no two edges share a common vertex. A bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets, U and V, such that every edge connects a vertex in U to one in V.

This algorithm is useful in various applications, including:
*   **Assignment Problems**: Assigning workers to tasks where each worker can only do certain tasks.
*   **Resource Allocation**: Matching available resources to demands.
*   **Network Flow**: As a sub-problem in more complex network flow scenarios.

## Usage

To use the `BipartiteMatching` class, you first create an instance, specifying the number of vertices in each partition. Then, you add edges between the partitions. Finally, you call the `max_matching()` method to get the size of the maximum matching and the list of matched edges.


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

# Example Usage:
# Create a bipartite graph with 4 vertices on the left (U) and 4 on the right (V)
# bm = BipartiteMatching(4, 4)

# Add edges (from left partition to right partition)
# bm.add_edge(0, 1)
# bm.add_edge(0, 2)
# bm.add_edge(1, 0)
# bm.add_edge(2, 1)
# bm.add_edge(3, 2)
# bm.add_edge(3, 3)

# Compute the maximum matching
# size, matched_edges = bm.max_matching()

# print(f"Maximum Matching Size: {size}")
# print(f"Matched Edges: {matched_edges}")
# Expected Output:
# Maximum Matching Size: 3
# Matched Edges: [(0, 2), (1, 0), (3, 3)] or similar valid matching


## Detailed Explanation

The `BipartiteMatching` class models a bipartite graph and finds its maximum cardinality matching.

1.  **Initialization (`__init__`)**: The constructor takes the number of vertices in the left partition (`num_left`) and the right partition (`num_right`). It initializes an adjacency list `self.adj` where `self.adj[u]` stores a list of vertices in the right partition that vertex `u` (from the left partition) is connected to.

2.  **Adding Edges (`add_edge`)**: This method allows you to define the connections in the bipartite graph. An edge is added from vertex `u` in the left partition to vertex `v` in the right partition. Basic validation is performed to ensure vertex indices are within bounds.

3.  **Depth-First Search for Augmenting Paths (`_dfs`)**: This is the core recursive helper function. It attempts to find an *augmenting path* starting from a given left vertex `u`. An augmenting path is a path that starts at an unmatched vertex in U, alternates between unmatched and matched edges, and ends at an unmatched vertex in V. If such a path is found:
    *   It means we can increase the size of the matching by flipping the status of edges along this path (unmatched becomes matched, and matched becomes unmatched).
    *   The function returns `True` to indicate success.
    *   The `match_right` array is updated to reflect the new matching.
    *   `visited` array is used to prevent cycles and redundant exploration within a single DFS call.

4.  **Maximum Matching Calculation (`max_matching`)**: This method orchestrates the matching process:
    *   It initializes `match_right`, an array where `match_right[v]` stores the vertex from the left partition that vertex `v` (from the right partition) is currently matched with. Initially, all right vertices are unmatched (`-1`).
    *   It iterates through each vertex `u` in the left partition.
    *   For each `u`, it calls `_dfs` to try and find an augmenting path starting from `u`. A fresh `visited` array is used for each `u` to ensure that paths explored for one starting vertex don't interfere with others.
    *   If `_dfs` returns `True`, it means an augmenting path was found and the matching was successfully augmented, so `matching_size` is incremented.
    *   After iterating through all left vertices, `matching_size` holds the cardinality of the maximum matching.
    *   Finally, it constructs and returns a list of `(u, v)` tuples representing the actual matched edges based on the final `match_right` array.

## Complexity Analysis

Let `|U|` be the number of vertices in the left partition, `|V|` be the number of vertices in the right partition, and `|E|` be the number of edges in the bipartite graph.

*   **Time Complexity**: The Ford-Fulkerson algorithm's complexity depends on how augmenting paths are found. With DFS, in the worst case, each call to `_dfs` might traverse all edges. Since `max_matching` calls `_dfs` for each vertex in `U`, and each `_dfs` can take `O(E)` time, the total time complexity is **O(|U| * |E|)**.

*   **Space Complexity**: The space complexity is dominated by the adjacency list representation of the graph and the auxiliary arrays used during DFS.
    *   Adjacency list: `O(|U| + |E|)`
    *   `match_right` array: `O(|V|)`
    *   `visited` array: `O(|V|)`
    *   Recursion stack for DFS: `O(|U| + |V|)` in the worst case.
    Therefore, the overall space complexity is **O(|U| + |V| + |E|)**.
