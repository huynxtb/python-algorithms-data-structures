from typing import Callable, Iterable, List, Tuple, Dict, Hashable
import heapq

def _reconstruct_path(came_from: Dict[Hashable, Hashable], current: Hashable) -> List[Hashable]:
    """
    Helper function to reconstruct the path from the 'came_from' dictionary.
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def a_star_search(
    start: Hashable,
    goal: Hashable,
    get_neighbors: Callable[[Hashable], Iterable[Tuple[Hashable, float]]],
    heuristic: Callable[[Hashable], float]
) -> Tuple[List[Hashable] | None, float]:
    """
    Implements the A* search algorithm to find the shortest path between two nodes
    in a weighted graph.

    Args:
        start: The starting node. Must be hashable.
        goal: The target node. Must be hashable.
        get_neighbors: A callable that takes a node and returns an iterable of
                       (neighbor_node, edge_cost) tuples. 'edge_cost' must be a float.
        heuristic: A callable that takes a node and returns its estimated cost
                   to the goal node (h-score). This estimate must be non-negative.

    Returns:
        A tuple containing:
        - A list of nodes representing the optimal path from start to goal,
          or None if no path exists.
        - The total cost of the optimal path, or float('inf') if no path exists.
    """
    # The open_set is a min-heap storing (f_score, node) tuples.
    # f_score is the estimated total cost from start to goal through node.
    open_set: List[Tuple[float, Hashable]] = []
    heapq.heappush(open_set, (heuristic(start), start))

    # came_from maps each node to the node immediately preceding it on the
    # cheapest path from start found so far.
    came_from: Dict[Hashable, Hashable] = {}

    # g_score maps each node to the cost of the cheapest path from start to that node found so far.
    g_score: Dict[Hashable, float] = {start: 0.0}

    # f_score maps each node to the estimated total cost from start to goal through that node.
    # f_score[n] = g_score[n] + heuristic(n).
    f_score: Dict[Hashable, float] = {start: heuristic(start)}

    while open_set:
        # Pop the node with the lowest f_score from the open set.
        current_f_score, current_node = heapq.heappop(open_set)

        # If we already found a better path to current_node, this entry in the heap is outdated.
        # This check is crucial for efficiency as heapq doesn't support efficient key updates.
        if current_f_score > f_score.get(current_node, float('inf')):
            continue

        # If the current node is the goal, we have found the shortest path.
        if current_node == goal:
            path = _reconstruct_path(came_from, current_node)
            return path, g_score[current_node]

        # Explore neighbors of the current node.
        for neighbor, edge_cost in get_neighbors(current_node):
            # tentative_g_score is the cost from start to neighbor through current_node.
            tentative_g_score = g_score[current_node] + edge_cost

            # If this path to neighbor is better than any previous one, record it.
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # If the open set becomes empty and the goal was never reached, then no path exists.
    return None, float('inf')