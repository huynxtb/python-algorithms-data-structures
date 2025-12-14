from collections import deque

class Graph:
    def __init__(self, adjacency_list=None):
        """Initialize the graph with an optional adjacency list.

        adjacency_list should be a dictionary where keys are nodes and values
        are lists or sets of neighbors.
        """
        if adjacency_list is None:
            adjacency_list = {}
        self.adjacency_list = adjacency_list

    def bfs(self, start_node):
        """Perform BFS traversal starting from start_node.

        Args:
            start_node: The node from which BFS traversal begins.

        Returns:
            A list containing nodes in the order they were visited.
        """
        visited = set()
        order = []
        queue = deque()

        visited.add(start_node)
        queue.append(start_node)

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order
