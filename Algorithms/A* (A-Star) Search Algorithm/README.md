# A* (A-Star) Search Algorithm

## 1. Introduction

The A* (pronounced "A-star") search algorithm is a widely used, efficient, and optimal pathfinding algorithm. It is a graph traversal and path search algorithm that finds the shortest path between a starting node and a target node in a weighted graph. A* combines features of Dijkstra's algorithm (which guarantees finding the shortest path) and Greedy Best-First Search (which uses a heuristic to guide its search). This combination allows A* to be both optimal (finds the shortest path) and efficient (explores fewer nodes than Dijkstra's in many cases).

A* is particularly useful in scenarios where you need to find the shortest path in a graph where edge weights represent costs (e.g., distance, time, energy consumption) and an estimate of the remaining cost to the goal (heuristic) is available. Common applications include game AI (for character movement), robotics (path planning), network routing, and logistics.

For A* to guarantee optimality, the heuristic function must be *admissible* (never overestimates the cost to reach the goal) and ideally *consistent* (monotone, meaning the estimated cost from a node to the goal is less than or equal to the cost of moving to a neighbor plus the estimated cost from that neighbor to the goal).

## 2. Usage

To use the `a_star_search` function, you need to provide a starting node, a goal node, a function to retrieve neighbors and their edge costs, and a heuristic function. Below is a comprehensive example:


from a_star_search import a_star_search # Assuming the code is saved as a_star_search.py

# Define a sample graph where nodes are strings and edge costs are floats.
# Example: 'A': [('B', 1.0), ('C', 3.0)] means from A to B costs 1.0, from A to C costs 3.0.
graph = {
    'A': [('B', 1.0), ('C', 3.0)],
    'B': [('D', 2.0)],
    'C': [('D', 0.5), ('E', 4.0)],
    'D': [('E', 1.0)],
    'E': []
}

# Define the get_neighbors callable.
# It takes a node and returns an iterable of (neighbor, edge_cost) tuples.
def get_neighbors_func(node):
    return graph.get(node, [])

# Define the heuristic callable.
# It takes a node and returns its estimated cost to the goal.
# For this example, we'll use pre-defined heuristic values. In a real-world
# scenario (e.g., grid pathfinding), this might be Manhattan distance or Euclidean distance.
# The heuristic must be admissible (never overestimates the true cost).
heuristic_values = {
    'A': 5.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'E': 0.0, 'F': float('inf') # 'F' is not in graph
}
def heuristic_func(node):
    return heuristic_values.get(node, float('inf')) # Return infinity for unknown nodes

# --- Example 1: Finding a path ---
start_node_1 = 'A'
goal_node_1 = 'E'

print(f"Searching path from {start_node_1} to {goal_node_1}:")
path_1, cost_1 = a_star_search(start_node_1, goal_node_1, get_neighbors_func, heuristic_func)

if path_1:
    print(f"  Optimal path: {path_1}")
    print(f"  Total path cost: {cost_1}")
else:
    print(f"  No path found.")

print("\n" + "-"*30 + "\n")

# --- Example 2: No path exists ---
start_node_2 = 'F' # Node 'F' is not connected to the graph
goal_node_2 = 'E'

print(f"Searching path from {start_node_2} to {goal_node_2}:")
path_2, cost_2 = a_star_search(start_node_2, goal_node_2, get_neighbors_func, heuristic_func)

if path_2:
    print(f"  Optimal path: {path_2}")
    print(f"  Total path cost: {cost_2}")
else:
    print(f"  No path found. Cost: {cost_2}")


## 3. Detailed Explanation

The A* algorithm works by maintaining and evaluating nodes based on an estimated total cost function `f(n) = g(n) + h(n)`:

*   `g(n)`: The actual cost from the `start` node to the current node `n`. This is the accumulated cost of the path found so far.
*   `h(n)`: The estimated cost (heuristic) from the current node `n` to the `goal` node. This estimate guides the search towards the goal.

Here's how the implementation works:

1.  **Initialization:**
    *   `open_set`: A min-priority queue (implemented using `heapq`) stores `(f_score, node)` tuples. Nodes are extracted from this set based on the lowest `f_score`, meaning the most promising node is explored next.
    *   `came_from`: A dictionary to reconstruct the path. `came_from[node]` stores the node immediately preceding `node` on the cheapest path found to `node` so far.
    *   `g_score`: A dictionary storing the actual cost from the `start` node to each node. Initially, `g_score[start]` is `0.0`, and all other nodes are implicitly `float('inf')`.
    *   `f_score`: A dictionary storing the estimated total cost from `start` to `goal` through each node. `f_score[start]` is initialized to `heuristic(start)`, and others are implicitly `float('inf')`.
    *   The `start` node is pushed onto the `open_set` with its initial `f_score`.

2.  **Main Loop:**
    *   The algorithm continues as long as there are nodes in the `open_set`.
    *   In each iteration, it extracts the `current_node` with the lowest `f_score` from `open_set`.
    *   **Outdated Entry Check:** A crucial optimization: if the `current_f_score` (from the heap) is greater than the `f_score` currently recorded in the `f_score` dictionary for `current_node`, it means a shorter path to `current_node` has already been found and processed. This outdated entry is skipped.
    *   **Goal Check:** If `current_node` is the `goal`, the shortest path has been found. The path is reconstructed by tracing back through the `came_from` dictionary, and the path and its total cost are returned.
    *   **Neighbor Exploration:** For each `neighbor` of `current_node`:
        *   A `tentative_g_score` is calculated: `g_score[current_node] + edge_cost`.
        *   If this `tentative_g_score` is less than the currently known `g_score` for `neighbor` (meaning a shorter path to `neighbor` has been found via `current_node`):
            *   `came_from[neighbor]` is updated to `current_node`.
            *   `g_score[neighbor]` is updated to `tentative_g_score`.
            *   `f_score[neighbor]` is updated to `tentative_g_score + heuristic(neighbor)`.
            *   The `(f_score[neighbor], neighbor)` tuple is pushed onto the `open_set`.

3.  **No Path Found:** If the `open_set` becomes empty and the `goal` was never reached, it means no path exists from `start` to `goal`. In this case, `(None, float('inf'))` is returned.

## 4. Complexity Analysis

Let `V` be the number of nodes (vertices) and `E` be the number of edges in the graph.

*   **Time Complexity:**
    *   **Worst Case:** O(E log V). In the worst case (e.g., when the heuristic is non-informative or misleading), A* might explore as many nodes as Dijkstra's algorithm. Each node can be added to the priority queue (heap) at most once, and each `heapq.heappush` or `heapq.heappop` operation takes O(log V) time. Each edge is processed at most once. Therefore, the total time complexity is dominated by heap operations, resulting in O(E log V).
    *   **Best Case / Average Case:** With an effective (admissible and consistent) heuristic, A* can be significantly faster than Dijkstra's, as it prunes large parts of the search space. The actual performance depends heavily on the quality of the heuristic.

*   **Space Complexity:**
    *   O(V + E). In the worst case, the `open_set` (priority queue), `came_from`, `g_score`, and `f_score` dictionaries might need to store information for all `V` nodes. The `get_neighbors` function might implicitly represent `E` edges. Therefore, the space complexity is proportional to the size of the graph.