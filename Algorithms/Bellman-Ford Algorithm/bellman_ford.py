class NegativeCycleError(Exception):
    """Raised when a negative-weight cycle is detected in the graph."""
    pass


def bellman_ford(
    vertices_count: int,
    edges: list[tuple[int, int, float]],
    source: int
) -> tuple[dict[int, float], dict[int, int | None]]:
    """
    Computes shortest paths from a single source vertex to all other vertices.
    Detects negative-weight cycles.
    """
    distances: dict[int, float] = {i: float('inf') for i in range(vertices_count)}
    predecessors: dict[int, int | None] = {i: None for i in range(vertices_count)}
    
    distances[source] = 0.0
    
    # Relax edges |V| - 1 times
    for _ in range(vertices_count - 1):
        any_update = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                any_update = True
        if not any_update:
            break
            
    # Check for negative-weight cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise NegativeCycleError("Graph contains a negative-weight cycle")
            
    return distances, predecessors
