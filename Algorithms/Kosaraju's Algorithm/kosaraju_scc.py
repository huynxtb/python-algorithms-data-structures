from typing import List, Dict

class KosarajuSCC:
    """
    An implementation of Kosaraju's Algorithm to find Strongly Connected Components (SCCs)
    in a directed graph.
    """
    def __init__(self, vertices: int) -> None:
        """
        Initializes the graph with a specified number of vertices.
        Vertices are assumed to be 0-indexed from 0 to vertices - 1.
        """
        self.vertices = vertices
        self.adj: Dict[int, List[int]] = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int) -> None:
        """
        Adds a directed edge from vertex u to vertex v.
        """
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj[u].append(v)
        else:
            raise ValueError("Vertex index out of bounds.")

    def _fill_order(self, v: int, visited: List[bool], stack: List[int]) -> None:
        """
        Helper method to perform DFS and push vertices to the stack based on their finishing times.
        """
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self._fill_order(neighbor, visited, stack)
        stack.append(v)

    def _get_transpose(self) -> Dict[int, List[int]]:
        """
        Helper method to transpose the graph (reverse all directed edges).
        """
        transpose_adj: Dict[int, List[int]] = {i: [] for i in range(self.vertices)}
        for u in range(self.vertices):
            for v in self.adj[u]:
                transpose_adj[v].append(u)
        return transpose_adj

    def _dfs_collect(self, v: int, visited: List[bool], component: List[int], transpose_adj: Dict[int, List[int]]) -> None:
        """
        Helper method to perform DFS on the transposed graph and collect vertices in the current SCC.
        """
        visited[v] = True
        component.append(v)
        for neighbor in transpose_adj[v]:
            if not visited[neighbor]:
                self._dfs_collect(neighbor, visited, component, transpose_adj)

    def find_sccs(self) -> List[List[int]]:
        """
        Finds and returns all strongly connected components in the graph.
        
        Returns:
            List[List[int]]: A list of components, where each component is a list of vertices.
        """
        stack: List[int] = []
        visited = [False] * self.vertices

        # Step 1: Fill vertices in stack according to their finishing times
        for i in range(self.vertices):
            if not visited[i]:
                self._fill_order(i, visited, stack)

        # Step 2: Transpose the graph
        transpose_adj = self._get_transpose()

        # Step 3: Process all vertices in order defined by stack
        visited = [False] * self.vertices
        sccs: List[List[int]] = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component: List[int] = []
                self._dfs_collect(v, visited, component, transpose_adj)
                sccs.append(component)

        return sccs