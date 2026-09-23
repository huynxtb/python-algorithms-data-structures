from typing import List, Tuple, Set, Dict, Any

class Graph:
    """Represents a directed or undirected graph using an adjacency list."""

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.adjacency_list: Dict[Any, List[Any]] = {}

    def add_edge(self, u: Any, v: Any, bidirectional: bool = True) -> None:
        """Add an edge between nodes u and v.
        
        Args:
            u: Source node.
            v: Destination node.
            bidirectional: If True, creates edges in both directions. Defaults to True.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        
        self.adjacency_list[u].append(v)
        if bidirectional:
            self.adjacency_list[v].append(u)

    def get_neighbors(self, node: Any) -> List[Any]:
        """Return the list of neighbors for a given node.
        
        Args:
            node: The node to get neighbors for.
            
        Returns:
            List of neighboring nodes, or empty list if node not in graph.
        """
        return self.adjacency_list.get(node, [])


def depth_limited_search(graph: Graph, source: Any, target: Any, limit: int) -> Tuple[bool, List[Any]]:
    """Perform depth-limited DFS from source looking for target.
    
    Args:
        graph: The graph to search.
        source: The starting node.
        target: The node to find.
        limit: Maximum depth to explore.
        
    Returns:
        Tuple of (found, path) where found is True if target was reached,
        and path is the list of nodes from source to target (empty if not found).
    """
    visited: Set[Any] = set()
    
    def dls_recursive(node: Any, target: Any, depth: int, path: List[Any]) -> Tuple[bool, List[Any]]:
        """Recursive helper function for depth-limited search.
        
        Args:
            node: Current node being explored.
            target: The target node to find.
            depth: Current depth in the search.
            path: Current path from source to node.
            
        Returns:
            Tuple of (found, path) indicating success and the path taken.
        """
        visited.add(node)
        current_path = path + [node]
        
        if node == target:
            return (True, current_path)
        
        if depth == 0:
            return (False, [])
        
        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                found, result_path = dls_recursive(neighbor, target, depth - 1, current_path)
                if found:
                    return (True, result_path)
        
        return (False, [])
    
    if source not in graph.adjacency_list:
        return (False, [])
    
    found, path = dls_recursive(source, target, limit, [])
    return (found, path)


def iddfs(graph: Graph, source: Any, target: Any, max_depth: int) -> Tuple[bool, List[Any], int]:
    """Perform Iterative Deepening DFS from source looking for target.
    
    Args:
        graph: The graph to search.
        source: The starting node.
        target: The node to find.
        max_depth: Maximum depth to search up to.
        
    Returns:
        Tuple of (found, path, depth_found) where found indicates success,
        path is the nodes from source to target, and depth_found is the depth
        at which target was found (or -1 if not found).
    """
    if source == target:
        return (True, [source], 0)
    
    if source not in graph.adjacency_list:
        return (False, [], -1)
    
    for depth_limit in range(max_depth + 1):
        found, path = depth_limited_search(graph, source, target, depth_limit)
        if found:
            return (True, path, depth_limit)
    
    return (False, [], -1)


def iddfs_all_paths(graph: Graph, source: Any, target: Any, max_depth: int) -> Tuple[List[List[Any]], int]:
    """Find all shortest paths from source to target using IDDFS.
    
    Args:
        graph: The graph to search.
        source: The starting node.
        target: The node to find.
        max_depth: Maximum depth to search up to.
        
    Returns:
        Tuple of (paths, depth_found) where paths is a list of all shortest paths
        from source to target, and depth_found is the depth at which they were found
        (or -1 if no paths exist).
    """
    if source == target:
        return ([source], 0)
    
    if source not in graph.adjacency_list:
        return ([], -1)
    
    def find_all_paths_limited(graph: Graph, source: Any, target: Any, limit: int) -> List[List[Any]]:
        """Find all paths from source to target within depth limit.
        
        Args:
            graph: The graph to search.
            source: The starting node.
            target: The target node.
            limit: Maximum depth to explore.
            
        Returns:
            List of all paths found from source to target within the depth limit.
        """
        all_paths: List[List[Any]] = []
        visited: Set[Any] = set()
        
        def dfs_all(node: Any, target: Any, depth: int, path: List[Any]) -> None:
            """Recursive helper to find all paths.
            
            Args:
                node: Current node.
                target: Target node.
                depth: Current depth.
                path: Current path from source.
            """
            if node == target:
                all_paths.append(path + [node])
                return
            
            if depth == 0:
                return
            
            visited.add(node)
            for neighbor in graph.get_neighbors(node):
                if neighbor not in visited:
                    dfs_all(neighbor, target, depth - 1, path + [node])
            visited.discard(node)
        
        dfs_all(source, target, limit, [])
        return all_paths
    
    for depth_limit in range(max_depth + 1):
        paths = find_all_paths_limited(graph, source, target, depth_limit)
        if paths:
            return (paths, depth_limit)
    
    return ([], -1)
