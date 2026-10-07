from collections import deque
from typing import Any, Dict, Optional, Set


class HopcroftKarp:
    """
    Hopcroft-Karp algorithm for finding Maximum Cardinality Matching in unweighted bipartite graphs.

    The algorithm operates in phases combining Breadth-First Search (BFS) and Depth-First Search (DFS).
    In each phase:
      1. BFS partitions vertices into alternating distance layers starting from all unmatched left vertices
         and identifies the shortest augmenting path length.
      2. DFS searches for a maximal set of vertex-disjoint shortest augmenting paths along the layered graph
         and augments the current matching.

    Time Complexity:
      - Total: O(E * sqrt(V)), where V is the total number of vertices and E is the number of edges.
      - Per Phase: O(V + E).
      - Maximum number of phases: O(sqrt(V)).

    Space Complexity:
      - O(V + E) auxiliary space for matchings, distances, and adjacency representation.
    """

    # Sentinel object representing the "dummy" / unmatched nil vertex.
    _NIL: object = object()

    def __init__(
        self,
        left_vertices: Set[Any],
        right_vertices: Set[Any],
        edges: Dict[Any, Set[Any]],
    ) -> None:
        """
        Initialize the bipartite graph partitions and adjacency list.

        :param left_vertices: Set of vertices in the left partition (U).
        :param right_vertices: Set of vertices in the right partition (V).
        :param edges: Mapping from each left vertex u in U to a set of adjacent right vertices v in V.
        """
        self._left_vertices: Set[Any] = set(left_vertices)
        self._right_vertices: Set[Any] = set(right_vertices)
        self._adj: Dict[Any, Set[Any]] = {
            u: set(neighbors) for u, neighbors in edges.items() if u in self._left_vertices
        }
        for u in self._left_vertices:
            if u not in self._adj:
                self._adj[u] = set()

        # Matching maps: vertex -> matched vertex (or _NIL if unmatched)
        self._pair_left: Dict[Any, Any] = {}
        self._pair_right: Dict[Any, Any] = {}

        # Distance map for vertices in the left partition and _NIL
        self._dist: Dict[Any, float] = {}

    def _bfs(self) -> bool:
        """
        Perform Breadth-First Search from all currently unmatched vertices in the left partition.

        Computes distance layers along alternating paths and determines the existence of augmenting paths.

        :return: True if at least one augmenting path exists to an unmatched right vertex (reaching _NIL),
                 False otherwise.
        """
        queue: deque = deque()
        inf = float("inf")

        for u in self._left_vertices:
            if self._pair_left[u] is self._NIL:
                self._dist[u] = 0.0
                queue.append(u)
            else:
                self._dist[u] = inf

        self._dist[self._NIL] = inf

        while queue:
            u = queue.popleft()

            # If we've found a path reaching NIL at a distance shorter than or equal to current u,
            # we do not expand beyond this layer to maintain shortest augmenting path property.
            if self._dist[u] < self._dist[self._NIL]:
                for v in self._adj[u]:
                    next_u = self._pair_right[v]
                    if self._dist[next_u] == inf:
                        self._dist[next_u] = self._dist[u] + 1.0
                        queue.append(next_u)

        return self._dist[self._NIL] != inf

    def _dfs(self, u: Any) -> bool:
        """
        Perform Depth-First Search to find vertex-disjoint augmenting paths in the layered graph.

        If an augmenting path is found, the matching along the path is immediately augmented.

        :param u: The current vertex in the left partition (or _NIL).
        :return: True if an augmenting path starting at u is found, False otherwise.
        """
        if u is self._NIL:
            return True

        inf = float("inf")
        for v in self._adj[u]:
            next_u = self._pair_right[v]
            if self._dist[next_u] == self._dist[u] + 1.0:
                if self._dfs(next_u):
                    self._pair_right[v] = u
                    self._pair_left[u] = v
                    return True

        # Mark as visited / non-viable for this phase to prevent repeated failed traversals
        self._dist[u] = inf
        return False

    def max_matching(self) -> Dict[Any, Any]:
        """
        Execute the Hopcroft-Karp algorithm to compute the Maximum Cardinality Matching.

        Alternates between BFS (layered graph construction) and DFS (path augmentation)
        until no more augmenting paths can be found.

        :return: A dictionary mapping each matched left vertex to its matched right vertex counterpart.
        """
        # Initialize all vertices as unmatched (paired with _NIL)
        for u in self._left_vertices:
            self._pair_left[u] = self._NIL
        for v in self._right_vertices:
            self._pair_right[v] = self._NIL

        # Main loop: run phases while augmenting paths exist
        while self._bfs():
            for u in self._left_vertices:
                if self._pair_left[u] is self._NIL:
                    self._dfs(u)

        # Filter out unmatched vertices from the result
        matching: Dict[Any, Any] = {
            u: self._pair_left[u]
            for u in self._left_vertices
            if self._pair_left[u] is not self._NIL
        }

        return matching
