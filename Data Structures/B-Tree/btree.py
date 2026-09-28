from typing import Generic, List, Optional, Tuple, TypeVar

T = TypeVar('T')


class BTreeNode(Generic[T]):
    """
    A node in a B-Tree.

    Attributes:
        keys (List[T]): The list of keys stored in the node.
        children (List[BTreeNode[T]]): Pointers to child nodes.
        leaf (bool): True if the node is a leaf, False otherwise.
    """

    def __init__(self, leaf: bool = True) -> None:
        self.keys: List[T] = []
        self.children: List[BTreeNode[T]] = []
        self.leaf: bool = leaf

    def find_key(self, key: T) -> int:
        """
        Find the index of the first key that is greater than or equal to the given key.

        Args:
            key (T): Key to search for.

        Returns:
            int: The index of the first key >= key.
        """
        idx = 0
        while idx < len(self.keys) and self.keys[idx] < key:
            idx += 1
        return idx


class BTree(Generic[T]):
    """
    A B-Tree data structure parameterized by a minimum degree `t`.

    In a B-Tree of minimum degree `t` (t >= 2):
      - Every node other than the root must contain at least t - 1 keys.
      - Every node may contain at most 2t - 1 keys.
      - Every internal node other than the root has at least t children.
      - Every internal node has at most 2t children.
      - All leaves are at the same depth.
    """

    def __init__(self, t: int = 2) -> None:
        """
        Initialize the B-Tree with a minimum degree `t`.

        Args:
            t (int): Minimum degree (must be >= 2).
        """
        if t < 2:
            raise ValueError("Minimum degree 't' must be at least 2.")
        self.t: int = t
        self.root: BTreeNode[T] = BTreeNode[T](leaf=True)

    def search(self, key: T) -> Optional[Tuple[BTreeNode[T], int]]:
        """
        Search for a key in the B-Tree.

        Args:
            key (T): The key to search for.

        Returns:
            Optional[Tuple[BTreeNode[T], int]]: A tuple of (node, index) if found, else None.
        """
        return self._search(self.root, key)

    def _search(self, node: BTreeNode[T], key: T) -> Optional[Tuple[BTreeNode[T], int]]:
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        if node.leaf:
            return None
        return self._search(node.children[i], key)

    def insert(self, key: T) -> None:
        """
        Insert a new key into the B-Tree.

        Args:
            key (T): The key to insert.
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode[T](leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0, self.root)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _split_child(self, parent: BTreeNode[T], index: int, full_child: BTreeNode[T]) -> None:
        t = self.t
        new_sibling = BTreeNode[T](leaf=full_child.leaf)

        median_key = full_child.keys[t - 1]

        new_sibling.keys = full_child.keys[t:(2 * t - 1)]
        full_child.keys = full_child.keys[0:(t - 1)]

        if not full_child.leaf:
            new_sibling.children = full_child.children[t:(2 * t)]
            full_child.children = full_child.children[0:t]

        parent.children.insert(index + 1, new_sibling)
        parent.keys.insert(index, median_key)

    def _insert_non_full(self, node: BTreeNode[T], key: T) -> None:
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(key)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i, node.children[i])
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def delete(self, key: T) -> None:
        """
        Delete a key from the B-Tree.

        Args:
            key (T): The key to remove.
        """
        self._delete(self.root, key)

        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node: BTreeNode[T], key: T) -> None:
        t = self.t
        idx = node.find_key(key)

        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                node.keys.pop(idx)
            else:
                self._delete_internal_node(node, idx)
        else:
            if node.leaf:
                return

            flag = idx == len(node.keys)

            if len(node.children[idx].keys) < t:
                self._fill(node, idx)

            if flag and idx > len(node.keys):
                self._delete(node.children[idx - 1], key)
            else:
                self._delete(node.children[idx], key)

    def _delete_internal_node(self, node: BTreeNode[T], idx: int) -> None:
        k = node.keys[idx]
        t = self.t

        if len(node.children[idx].keys) >= t:
            pred = self._get_predecessor(node, idx)
            node.keys[idx] = pred
            self._delete(node.children[idx], pred)
        elif len(node.children[idx + 1].keys) >= t:
            succ = self._get_successor(node, idx)
            node.keys[idx] = succ
            self._delete(node.children[idx + 1], succ)
        else:
            self._merge(node, idx)
            self._delete(node.children[idx], k)

    def _get_predecessor(self, node: BTreeNode[T], idx: int) -> T:
        curr = node.children[idx]
        while not curr.leaf:
            curr = curr.children[-1]
        return curr.keys[-1]

    def _get_successor(self, node: BTreeNode[T], idx: int) -> T:
        curr = node.children[idx + 1]
        while not curr.leaf:
            curr = curr.children[0]
        return curr.keys[0]

    def _fill(self, node: BTreeNode[T], idx: int) -> None:
        t = self.t
        if idx != 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        else:
            if idx != len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node: BTreeNode[T], idx: int) -> None:
        child = node.children[idx]
        sibling = node.children[idx - 1]

        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node: BTreeNode[T], idx: int) -> None:
        child = node.children[idx]
        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node: BTreeNode[T], idx: int) -> None:
        child = node.children[idx]
        sibling = node.children[idx + 1]

        child.keys.append(node.keys.pop(idx))
        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        node.children.pop(idx + 1)

    def inorder_traversal(self) -> List[T]:
        """
        Return all keys in the B-Tree in sorted order.

        Returns:
            List[T]: Sorted list of all elements in the B-Tree.
        """
        result: List[T] = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node: Optional[BTreeNode[T]], result: List[T]) -> None:
        if node is not None:
            for i in range(len(node.keys)):
                if not node.leaf:
                    self._inorder_traversal(node.children[i], result)
                result.append(node.keys[i])
            if not node.leaf:
                self._inorder_traversal(node.children[len(node.keys)], result)
