from typing import Any, Optional, List


class SplayNode:
    """Represents a node in a Splay Tree."""

    def __init__(self, key: Any) -> None:
        self.key: Any = key
        self.left: Optional["SplayNode"] = None
        self.right: Optional["SplayNode"] = None
        self.parent: Optional["SplayNode"] = None


class SplayTree:
    """A self-adjusting Binary Search Tree using bottom-up splaying."""

    def __init__(self) -> None:
        self.root: Optional[SplayNode] = None
        self._size: int = 0

    def _right_rotate(self, node: SplayNode) -> None:
        """Perform a right rotation around the given node."""
        left_child = node.left
        if left_child is None:
            return

        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def _left_rotate(self, node: SplayNode) -> None:
        """Perform a left rotation around the given node."""
        right_child = node.right
        if right_child is None:
            return

        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def _splay(self, node: SplayNode) -> None:
        """Splay the given node to the root using bottom-up rotations."""
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                # Zig step
                if node == parent.left:
                    self._right_rotate(parent)
                else:
                    self._left_rotate(parent)
            elif node == parent.left and parent == grandparent.left:
                # Zig-Zig step (left-left)
                self._right_rotate(grandparent)
                self._right_rotate(parent)
            elif node == parent.right and parent == grandparent.right:
                # Zig-Zig step (right-right)
                self._left_rotate(grandparent)
                self._left_rotate(parent)
            elif node == parent.right and parent == grandparent.left:
                # Zig-Zag step (left-right)
                self._left_rotate(parent)
                self._right_rotate(grandparent)
            else:
                # Zig-Zag step (right-left)
                self._right_rotate(parent)
                self._left_rotate(grandparent)

    def insert(self, key: Any) -> None:
        """Insert a key into the splay tree and splay it to the root."""
        if self.root is None:
            self.root = SplayNode(key)
            self._size += 1
            return

        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Key already exists; splay the existing node
                self._splay(current)
                return

        new_node = SplayNode(key)
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._splay(new_node)
        self._size += 1

    def search(self, key: Any) -> bool:
        """Search for a key in the tree, splaying the accessed node to the root."""
        if self.root is None:
            return False

        current = self.root
        last = current
        while current is not None:
            last = current
            if key == current.key:
                self._splay(current)
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        self._splay(last)
        return False

    def _find_max(self, node: SplayNode) -> SplayNode:
        """Find and return the node with the maximum key in the subtree rooted at node."""
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, key: Any) -> None:
        """Delete a key from the splay tree."""
        if not self.search(key):
            raise KeyError(f"Key '{key}' not found in the tree.")

        # After search, the node to delete is at the root
        target = self.root
        if target.left is None:
            self.root = target.right
            if self.root is not None:
                self.root.parent = None
        elif target.right is None:
            self.root = target.left
            if self.root is not None:
                self.root.parent = None
        else:
            left_subtree = target.left
            left_subtree.parent = None
            right_subtree = target.right
            right_subtree.parent = None

            max_left = self._find_max(left_subtree)
            self.root = left_subtree
            self._splay(max_left)

            # max_left is now the root of left_subtree and has no right child
            self.root.right = right_subtree
            right_subtree.parent = self.root

        self._size -= 1

    def minimum(self) -> Any:
        """Return the minimum key in the tree, splaying it to the root."""
        if self.root is None:
            raise ValueError("Tree is empty.")

        current = self.root
        while current.left is not None:
            current = current.left
        self._splay(current)
        return current.key

    def maximum(self) -> Any:
        """Return the maximum key in the tree, splaying it to the root."""
        if self.root is None:
            raise ValueError("Tree is empty.")

        max_node = self._find_max(self.root)
        self._splay(max_node)
        return max_node.key

    def inorder(self) -> List[Any]:
        """Return a list of all keys in in-order (sorted) sequence."""
        result: List[Any] = []

        def _traverse(node: Optional[SplayNode]) -> None:
            if node is not None:
                _traverse(node.left)
                result.append(node.key)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def __contains__(self, key: Any) -> bool:
        """Membership check using search."""
        return self.search(key)

    def __len__(self) -> int:
        """Return the number of nodes in the tree."""
        return self._size

    def __bool__(self) -> bool:
        """Return True if the tree is non-empty, False otherwise."""
        return self.root is not None
