from collections import deque

class BFS:
    @staticmethod
    def traverse(graph, start_node):
        """
        Perform Breadth-First Search (BFS) on the graph starting from start_node.

        :param graph: dict, keys are nodes and values are lists of adjacent nodes
        :param start_node: the node to start traversal from
        :return: list of nodes in the order they are visited
        """
        visited = set()
        traversal_order = []
        queue = deque()

        visited.add(start_node)
        queue.append(start_node)

        while queue:
            current_node = queue.popleft()
            traversal_order.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order
