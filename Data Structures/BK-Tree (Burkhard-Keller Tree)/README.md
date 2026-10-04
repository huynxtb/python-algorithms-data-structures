### 1. Introduction

The Burkhard-Keller Tree (BK-Tree) is a metric tree data structure designed for efficient fuzzy string matching and nearest-neighbor searching in a metric space. Unlike binary search trees or tries, which are optimized for exact matches, a BK-Tree excels at finding items that are "close" to a given query, according to a defined distance metric.

It is particularly useful in applications such as:
*   **Spell checkers:** Suggesting corrections for misspelled words.
*   **Typo tolerance in search engines:** Finding relevant results despite minor errors in the query.
*   **Bioinformatics:** Searching for similar DNA sequences.
*   **Image retrieval:** Finding images similar to a query image based on feature vectors.

The core idea behind a BK-Tree is to organize items based on their distance from each other. Each node in the tree stores an item, and its children are organized by the distance from the parent's item. The tree leverages the triangle inequality property of metric spaces to prune large portions of the search space, significantly speeding up fuzzy searches.

### 2. Usage

To use the `BKTree`, you can instantiate it with an optional custom distance function. If no function is provided, it defaults to the Levenshtein distance, making it suitable for string matching.


from typing import Callable, Tuple, List

# Assume the BKTree and _levenshtein_distance are defined as above

# Example 1: Using default Levenshtein distance for strings
bk_tree_str = BKTree[str]()

words = ["book", "books", "cake", "cape", "cart", "car", "dark", "park", "spark"]
for word in words:
    bk_tree_str.insert(word)

print(f"Total words in tree: {len(bk_tree_str)}")

# Search for words within Levenshtein distance 1 of "caqe"
results_1 = bk_tree_str.search("caqe", 1)
print(f"Words within distance 1 of 'caqe': {results_1}")

# Search for words within Levenshtein distance 2 of "bark"
results_2 = bk_tree_str.search("bark", 2)
print(f"Words within distance 2 of 'bark': {results_2}")

# Check for exact existence
print(f"'book' in tree: {'book' in bk_tree_str}")
print(f"'apple' in tree: {'apple' in bk_tree_str}")


# Example 2: Using a custom distance function for a different type (e.g., tuples of integers)
# A simple custom distance function (Manhattan distance for 2D points)
def manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

bk_tree_points = BKTree[Tuple[int, int]](distance_func=manhattan_distance)

points = [(1, 1), (1, 2), (3, 3), (5, 5), (5, 6), (10, 10)]
for point in points:
    bk_tree_points.insert(point)

print(f"\nTotal points in tree: {len(bk_tree_points)}")

# Search for points within Manhattan distance 2 of (2, 2)
query_point = (2, 2)
results_points = bk_tree_points.search(query_point, 2)
print(f"Points within distance 2 of {query_point}: {results_points}")


### 3. Detailed Explanation

This implementation provides a `BKTree` class that can store any type `T` for which a metric distance function `d(T, T) -> int` is defined.

**Levenshtein Distance (`_levenshtein_distance`)**:
This private helper function calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. It uses dynamic programming with a space optimization: instead of storing the entire `m x n` matrix, it only keeps track of the previous row's distances, reducing space complexity from O(MN) to O(min(M, N)).

**`BKTreeNode` Class**:
Each node in the BK-Tree holds an `item` (the actual data) and a dictionary called `children`. The keys of this dictionary are integer distances, and the values are other `BKTreeNode` instances. If `node_A` has a child `node_B` at distance `d`, it means `self.distance_func(node_A.item, node_B.item)` equals `d`.

**`BKTree` Class**:
*   **Initialization (`__init__`)**:
    *   The tree is initialized with an optional `distance_func`. If `None`, it defaults to `_levenshtein_distance`, making the tree suitable for string items.
    *   `self.root`: The root node of the tree, initially `None`.
    *   `self._size`: Tracks the number of items in the tree.

*   **Insertion (`insert`)**:
    *   If the tree is empty, the first item becomes the root.
    *   Otherwise, the algorithm traverses the tree starting from the root. At each `current_node`, it calculates the distance `d` between the `item` to be inserted and `current_node.item`.
    *   If `d` is 0, the item is considered already present (or identical to an existing item), and insertion stops.
    *   If `current_node` already has a child for distance `d`, the traversal continues to that child.
    *   If no child exists for distance `d`, a new `BKTreeNode` is created for the `item` and added as a child of `current_node` at distance `d`.
    *   The `_size` is incremented upon successful insertion of a new item.

*   **Search (`search`)**:
    *   This method performs a breadth-first search (BFS) to find all items within `max_distance` of the `query`.
    *   It uses a `collections.deque` as a queue to manage nodes to visit.
    *   For each `current_node` popped from the queue:
        1.  The `distance_to_query` between `query` and `current_node.item` is calculated.
        2.  If `distance_to_query` is less than or equal to `max_distance`, `current_node.item` is added to the `results`.
        3.  **Triangle Inequality Pruning**: This is the core optimization. For each child `child_node` of `current_node` (connected by `child_edge_dist`), the algorithm checks if it's *possible* for `child_node.item` to be within `max_distance` of the `query`. The triangle inequality states that `d(A, C) >= |d(A, B) - d(B, C)|`. Here, `A` is `query`, `B` is `current_node.item`, and `C` is `child_node.item`. So, `d(query, child_node.item) >= |distance_to_query - child_edge_dist|`. If this lower bound `|distance_to_query - child_edge_dist|` is already greater than `max_distance`, then `child_node.item` *cannot* be a match, and that branch is pruned (not added to the queue). Otherwise, `child_node` is added to the queue for further exploration.
    *   Finally, the `results` list is sorted by distance.

*   **Length (`__len__`)**:
    Returns the count of items stored, maintained by `_size`.

*   **Contains (`__contains__`)**:
    Similar to `insert`, it traverses the tree. If an item with distance 0 to the query is found, it returns `True`. If a path for the item's distance is not found, it returns `False`.

### 4. Complexity Analysis

Let `N` be the number of items in the tree, `L` be the average length of an item (for string metrics), and `D` be the maximum depth of the tree. `C_d` denotes the time complexity of the `distance_func`.

*   **`_levenshtein_distance(s1, s2)`**:
    *   **Time Complexity**: O(len(s1) * len(s2)).
    *   **Space Complexity**: O(min(len(s1), len(s2))) due to space optimization.

*   **`BKTree.insert(item)`**:
    *   **Worst Case Time**: O(D * C_d). In a degenerate tree, `D` can be `N`, leading to O(N * C_d).
    *   **Average Case Time**: The depth of a BK-Tree is typically logarithmic or sub-linear with respect to `N` for many metric spaces, making average insertion closer to O(log N * C_d).
    *   **Space Complexity**: O(C_d) for distance calculation, plus O(item_size) for storing the item. Each insertion adds one node.

*   **`BKTree.search(query, max_distance)`**:
    *   **Worst Case Time**: O(N * C_d). This occurs if `max_distance` is very large (e.g., allowing all items to match) or if the tree structure is degenerate, requiring visits to many nodes.
    *   **Average Case Time**: Significantly better than worst-case due to pruning. It's often closer to O(k * C_d), where `k` is the number of nodes visited, which is typically much smaller than `N` and depends on the `max_distance` and the distribution of items.
    *   **Space Complexity**: O(W + R + C_d), where `W` is the maximum width of the queue during BFS, `R` is the size of the results list, and `C_d` is for distance calculation.

*   **`BKTree.__len__()`**:
    *   **Time Complexity**: O(1).
    *   **Space Complexity**: O(1).

*   **`BKTree.__contains__(item)`**:
    *   **Worst Case Time**: O(D * C_d). Similar to insertion, can be O(N * C_d) in a degenerate tree.
    *   **Average Case Time**: O(log N * C_d).
    *   **Space Complexity**: O(C_d).