from __future__ import annotations

import random
from typing import Any, Generic, Iterator, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class TreapNode(Generic[T]):
    """
    A node in a Treap storing a key, a priority, and subtree metadata.

    Attributes:
        key (T): The search key satisfying the Binary Search Tree property.
        priority (float): The randomized priority satisfying the Max-Heap property.
        left (Optional[TreapNode[T]]): Left child node.
        right (Optional[TreapNode[T]]): Right child node.
        size (int): Total number of nodes in the subtree rooted at this node.
    """

    __slots__ = ("key", "priority", "left", "right", "size")

    def __init__(self, key: T, priority: Optional[float] = None) -> None:
        self.key: T = key
        self.priority: float = random.random() if priority is None else priority
        self.left: Optional[TreapNode[T]] = None
        self.right: Optional[TreapNode[T]] = None
        self.size: int = 1

    def update_size(self) -> None:
        """Recalculate the size of the subtree rooted at this node."""
        left_size = self.left.size if self.left is not None else 0
        right_size = self.right.size if self.right is not None else 0
        self.size = 1 + left_size + right_size


class Treap(Generic[T]):
    """
    A randomized Cartesian Tree (Treap) implementation supporting dynamic insertions,
    deletions, membership tests, and order statistics in expected O(log n) time.
    """

    def __init__(self) -> None:
        """Initialize an empty Treap."""
        self._root: Optional[TreapNode[T]] = None

    @staticmethod
    def _get_size(node: Optional[TreapNode[T]]) -> int:
        """Return the size of a subtree, handling None nodes."""
        return node.size if node is not None else 0

    def _rotate_right(self, y: TreapNode[T]) -> TreapNode[T]:
        """
        Perform a right tree rotation.

        Args:
            y: The root of the subtree to rotate.

        Returns:
            The new root of the rotated subtree.
        """
        x = y.left
        if x is None:
            return y
        y.left = x.right
        x.right = y
        y.update_size()
        x.update_size()
        return x

    def _rotate_left(self, x: TreapNode[T]) -> TreapNode[T]:
        """
        Perform a left tree rotation.

        Args:
            x: The root of the subtree to rotate.

        Returns:
            The new root of the rotated subtree.
        """
        y = x.right
        if y is None:
            return x
        x.right = y.left
        y.left = x
        x.update_size()
        y.update_size()
        return y

    def _insert(self, node: Optional[TreapNode[T]], key: T, success: List[bool]) -> Optional[TreapNode[T]]:
        """
        Recursive helper to insert a key into the Treap.

        Args:
            node: Current subtree root.
            key: The key to insert.
            success: A single-element list tracking whether insertion took place.

        Returns:
            The updated root of the subtree.
        """
        if node is None:
            success[0] = True
            return TreapNode(key)

        if key == node.key:
            success[0] = False
            return node
        elif key < node.key:
            node.left = self._insert(node.left, key, success)
            if node.left is not None and node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, success)
            if node.right is not None and node.right.priority > node.priority:
                node = self._rotate_left(node)

        node.update_size()
        return node

    def insert(self, key: T) -> bool:
        """
        Insert a key into the Treap if not already present.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Args:
            key: The key to insert.

        Returns:
            True if the key was inserted, False if it was already present.
        """
        success = [False]
        self._root = self._insert(self._root, key, success)
        return success[0]

    def _delete(self, node: Optional[TreapNode[T]], key: T, success: List[bool]) -> Optional[TreapNode[T]]:
        """
        Recursive helper to remove a key from the Treap.

        Args:
            node: Current subtree root.
            key: The key to delete.
            success: A single-element list tracking whether deletion took place.

        Returns:
            The updated root of the subtree.
        """
        if node is None:
            success[0] = False
            return None

        if key < node.key:
            node.left = self._delete(node.left, key, success)
        elif key > node.key:
            node.right = self._delete(node.right, key, success)
        else:
            success[0] = True
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.priority > node.right.priority:
                    node = self._rotate_right(node)
                    node.right = self._delete(node.right, key, success)
                else:
                    node = self._rotate_left(node)
                    node.left = self._delete(node.left, key, success)

        if node is not None:
            node.update_size()
        return node

    def delete(self, key: T) -> bool:
        """
        Remove a key from the Treap.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Args:
            key: The key to delete.

        Returns:
            True if the key was found and deleted, False otherwise.
        """
        success = [False]
        self._root = self._delete(self._root, key, success)
        return success[0]

    def search(self, key: T) -> Optional[TreapNode[T]]:
        """
        Search for a node containing the specified key.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Args:
            key: The key to search for.

        Returns:
            The TreapNode matching the key, or None if not found.
        """
        curr = self._root
        while curr is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def __contains__(self, key: T) -> bool:
        """
        Check membership of a key in the Treap.

        Args:
            key: The key to check.

        Returns:
            True if the key is present, False otherwise.
        """
        return self.search(key) is not None

    def __len__(self) -> int:
        """
        Return the total number of elements in the Treap.

        Returns:
            The number of nodes in the Treap.
        """
        return self._get_size(self._root)

    def inorder(self) -> List[T]:
        """
        Perform an in-order traversal of the Treap.

        Returns:
            A list of keys in ascending sorted order.
        """
        result: List[T] = []
        stack: List[TreapNode[T]] = []
        curr = self._root

        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.key)
            curr = curr.right

        return result

    def __iter__(self) -> Iterator[T]:
        """Yield keys in ascending order via an iterator."""
        return iter(self.inorder())

    def find_kth_smallest(self, k: int) -> Optional[T]:
        """
        Find the k-th smallest element (1-indexed) in the Treap.

        Time Complexity:
            Average: O(log n)
            Worst: O(n)

        Args:
            k: 1-indexed rank of the desired element (1 <= k <= len(treap)).

        Returns:
            The k-th smallest key, or None if k is out of bounds.
        """
        if k <= 0 or k > len(self):
            return None

        curr = self._root
        while curr is not None:
            left_size = self._get_size(curr.left)
            rank = left_size + 1
            if k == rank:
                return curr.key
            elif k < rank:
                curr = curr.left
            else:
                k -= rank
                curr = curr.right
        return None
