import collections
from typing import TypeVar, Generic, Callable, Optional, List, Tuple, Dict

# Define a generic type for the items stored in the tree
T = TypeVar('T')

def _levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.
    This implementation uses dynamic programming with O(min(len(s1), len(s2))) space optimization.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The Levenshtein distance (number of edits) between s1 and s2.
    """
    if s1 == s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    # Ensure s1 is the shorter string for space optimization
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # dp array stores the distances for the current row
    # dp[j] will be the distance between s1[:i] and s2[:j]
    # Initialize dp array for the first row (s1 empty string)
    dp = list(range(len(s1) + 1))

    for i in range(1, len(s2) + 1):
        # prev_diag stores dp[j-1] from the previous row (dp[j-1] before update)
        # which is needed for the diagonal calculation
        prev_diag = dp[0] # Corresponds to dp[i-1][j-1]
        dp[0] = i # Distance for s1[:0] and s2[:i] is i (insert i chars)

        for j in range(1, len(s1) + 1):
            # temp stores dp[j] before it's updated, which becomes prev_diag for the next iteration
            temp = dp[j]
            cost = 0 if s1[j-1] == s2[i-1] else 1
            dp[j] = min(dp[j-1] + 1,      # Deletion
                        dp[j] + 1,        # Insertion (dp[j] here is dp[i-1][j])
                        prev_diag + cost) # Substitution (prev_diag here is dp[i-1][j-1])
            prev_diag = temp
    return dp[len(s1)]


class BKTreeNode(Generic[T]):
    """
    Represents a node in the BK-Tree.

    Each node stores an item and a dictionary of children, where keys are
    distances to the child's item and values are the child nodes themselves.
    """
    def __init__(self, item: T):
        """
        Initializes a BKTreeNode with the given item.

        Args:
            item: The item to store in this node.
        """
        self.item: T = item
        self.children: Dict[int, BKTreeNode[T]] = {}


class BKTree(Generic[T]):
    """
    A Burkhard-Keller Tree (BK-Tree) for efficient fuzzy string matching
    and nearest-neighbor searching in a metric space.

    It uses a user-defined distance function (defaulting to Levenshtein distance
    for strings) to organize items such that searches for items within a
    certain distance can be performed efficiently using the triangle inequality.
    """
    def __init__(self, distance_func: Optional[Callable[[T, T], int]] = None):
        """
        Initializes an empty BK-Tree.

        Args:
            distance_func: An optional callable that takes two items of type T
                           and returns an integer representing their distance.
                           This function must satisfy the properties of a metric space:
                           1. Non-negativity: d(x, y) >= 0
                           2. Identity of indiscernibles: d(x, y) = 0 iff x = y
                           3. Symmetry: d(x, y) = d(y, x)
                           4. Triangle inequality: d(x, z) <= d(x, y) + d(y, z)
                           If None, the Levenshtein distance is used, implying
                           that items must be strings.
        """
        self.root: Optional[BKTreeNode[T]] = None
        self._size: int = 0

        if distance_func is None:
            # Default to Levenshtein distance, assuming T is str
            # A runtime type check could be added here for robustness,
            # but for a generic type, it's often left to the user to ensure
            # type compatibility with the default function.
            self.distance_func: Callable[[T, T], int] = _levenshtein_distance # type: ignore
        else:
            self.distance_func = distance_func

    def insert(self, item: T) -> None:
        """
        Inserts an item into the BK-Tree.

        If the item already exists (i.e., its distance to an existing item is 0),
        it is not re-inserted.

        Args:
            item: The item to be inserted.
        """
        if self.root is None:
            self.root = BKTreeNode(item)
            self._size = 1
            return

        current_node = self.root
        while True:
            distance = self.distance_func(item, current_node.item)
            if distance == 0:
                # Item already exists or is identical to an existing item
                return

            if distance in current_node.children:
                current_node = current_node.children[distance]
            else:
                current_node.children[distance] = BKTreeNode(item)
                self._size += 1
                return

    def search(self, query: T, max_distance: int) -> List[Tuple[T, int]]:
        """
        Searches the BK-Tree for items within a specified maximum distance
        from the query item.

        The search uses the triangle inequality to prune branches of the tree
        that cannot contain matching items, significantly speeding up the process.

        Args:
            query: The item to search for.
            max_distance: The maximum allowed distance from the query item
                          for a match to be considered (inclusive).

        Returns:
            A list of tuples, where each tuple contains a matching item and its
            distance from the query. The list is sorted by ascending distance.
        """
        results: List[Tuple[T, int]] = []
        if self.root is None:
            return results

        # Use a deque for breadth-first search (BFS)
        # Stores nodes to visit
        queue = collections.deque([self.root])

        while queue:
            current_node = queue.popleft()
            distance_to_query = self.distance_func(query, current_node.item)

            if distance_to_query <= max_distance:
                results.append((current_node.item, distance_to_query))

            # Pruning using triangle inequality:
            # For any child 'C' of 'current_node' at distance 'd_parent_child',
            # and the query 'Q', we know:
            # |d(Q, current_node.item) - d_parent_child| <= d(Q, C.item) <= d(Q, current_node.item) + d_parent_child
            # If the lower bound of d(Q, C.item) is greater than max_distance,
            # then C.item cannot be within max_distance of Q.
            # So, we only need to explore children where:
            # |distance_to_query - child_edge_dist| <= max_distance
            for child_edge_dist, child_node in current_node.children.items():
                lower_bound_dist = abs(distance_to_query - child_edge_dist)
                if lower_bound_dist <= max_distance:
                    queue.append(child_node)

        # Sort results by distance for consistent output
        results.sort(key=lambda x: x[1])
        return results

    def __len__(self) -> int:
        """
        Returns the total number of items stored in the BK-Tree.
        """
        return self._size

    def __contains__(self, item: T) -> bool:
        """
        Checks if an exact item exists in the BK-Tree.

        Args:
            item: The item to check for existence.

        Returns:
            True if the item exists, False otherwise.
        """
        if self.root is None:
            return False

        current_node = self.root
        while True:
            distance = self.distance_func(item, current_node.item)
            if distance == 0:
                return True # Found an exact match

            if distance in current_node.children:
                current_node = current_node.children[distance]
            else:
                return False # No child at this distance, item not found
