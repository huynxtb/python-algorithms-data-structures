class MaxFlowEdmondsKarp:
    class Edge:
        def __init__(self, to, capacity, rev):
            self.to = to
            self.capacity = capacity
            self.rev = rev

    def __init__(self, vertex_count):
        self.size = vertex_count
        self.graph = [[] for _ in range(vertex_count)]

    def add_edge(self, frm, to, capacity):
        forward = self.Edge(to, capacity, len(self.graph[to]))
        backward = self.Edge(frm, 0, len(self.graph[frm]))
        self.graph[frm].append(forward)
        self.graph[to].append(backward)

    def bfs(self, source, sink, parent):
        visited = [False] * self.size
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)
            for i, e in enumerate(self.graph[u]):
                if not visited[e.to] and e.capacity > 0:
                    queue.append(e.to)
                    visited[e.to] = True
                    parent[e.to] = (u, i)
                    if e.to == sink:
                        return True
        return False

    def max_flow(self, source, sink):
        parent = [(-1, -1)] * self.size
        flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                u, i = parent[s]
                path_flow = min(path_flow, self.graph[u][i].capacity)
                s = u
            v = sink
            while v != source:
                u, i = parent[v]
                self.graph[u][i].capacity -= path_flow
                rev = self.graph[u][i].rev
                self.graph[v][rev].capacity += path_flow
                v = u
            flow += path_flow
        return flow

    def get_graph(self):
        return self.graph

    def get_size(self):
        return self.size
