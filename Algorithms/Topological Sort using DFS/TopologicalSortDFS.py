class GraphCycleError(Exception):
    """Exception raised when a cycle is detected in the graph."""
    pass

class DirectedGraph:
    def __init__(self):
        # adjacency list representation of the graph
        # keys are vertices, values are sets of adjacent vertices
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):
        # add vertices if they are not present
        if u not in self.adj:
            self.adj[u] = set()
        if v not in self.adj:
            self.adj[v] = set()
        self.adj[u].add(v)

    def topological_sort(self):
        """
        Perform a topological sort of the vertices in the graph using DFS.

        Returns:
            list: A list of vertices in topologically sorted order.

        Raises:
            GraphCycleError: If a cycle is detected in the graph.
        """
        # states: "unvisited", "visiting", and "visited"
        state = {v: "unvisited" for v in self.adj}
        topo_order = []

        def dfs(vertex):
            if state[vertex] == "visiting":
                # We encountered a cycle
                raise GraphCycleError(f"Cycle detected at vertex {vertex}")
            if state[vertex] == "unvisited":
                state[vertex] = "visiting"
                for neighbor in self.adj[vertex]:
                    dfs(neighbor)
                state[vertex] = "visited"
                topo_order.append(vertex)

        for vertex in self.adj:
            if state[vertex] == "unvisited":
                dfs(vertex)

        topo_order.reverse()  # reverse to get correct order
        return topo_order