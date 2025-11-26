class TarjanSCC:
    def __init__(self):
        self.index = 0
        self.stack = []
        self.on_stack = set()
        self.indexes = {}
        self.low_links = {}
        self.sccs = []

    def strongly_connected_components(self, graph):
        """
        Find strongly connected components in the given directed graph using Tarjan's algorithm.

        :param graph: dict, adjacency list representation of the graph
                      keys are nodes and values are lists of adjacent nodes
        :return: list of lists, each inner list is a strongly connected component
        """
        self.index = 0
        self.stack = []
        self.on_stack = set()
        self.indexes = {}
        self.low_links = {}
        self.sccs = []

        for node in graph:
            if node not in self.indexes:
                self._strongconnect(node, graph)

        return self.sccs

    def _strongconnect(self, node, graph):
        # Set the depth index for node to the smallest unused index
        self.indexes[node] = self.index
        self.low_links[node] = self.index
        self.index += 1
        self.stack.append(node)
        self.on_stack.add(node)

        # Consider successors of node
        for neighbor in graph.get(node, []):
            if neighbor not in self.indexes:
                # Successor neighbor has not yet been visited; recurse on it
                self._strongconnect(neighbor, graph)
                self.low_links[node] = min(self.low_links[node], self.low_links[neighbor])
            elif neighbor in self.on_stack:
                # Successor neighbor is in stack and hence in the current SCC
                self.low_links[node] = min(self.low_links[node], self.indexes[neighbor])

        # If node is a root node, pop the stack and generate an SCC
        if self.low_links[node] == self.indexes[node]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            self.sccs.append(scc)