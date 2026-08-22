from typing import Optional, List

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, val: int) -> None:
        """Inserts a value into the BST."""
        self.root = self._insert(self.root, val)

    def _insert(self, root: Optional[Node], val: int) -> Node:
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)
        return root

    def search(self, val: int) -> Optional[Node]:
        """Searches for a value in the BST and returns the node."""
        return self._search(self.root, val)

    def _search(self, root: Optional[Node], val: int) -> Optional[Node]:
        if root is None or root.val == val:
            return root
        if val < root.val:
            return self._search(root.left, val)
        return self._search(root.right, val)

    def delete(self, val: int) -> None:
        """Deletes a value from the BST."""
        self.root = self._delete(self.root, val)

    def _delete(self, root: Optional[Node], val: int) -> Optional[Node]:
        if root is None:
            return None
        if val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self) -> List[int]:
        """Returns a list of values from an inorder traversal."""
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root: Optional[Node], result: List[int]) -> None:
        if root:
            self._inorder(root.left, result)
            result.append(root.val)
            self._inorder(root.right, result)

    def preorder(self) -> List[int]:
        """Returns a list of values from a preorder traversal."""
        result: List[int] = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root: Optional[Node], result: List[int]) -> None:
        if root:
            result.append(root.val)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self) -> List[int]:
        """Returns a list of values from a postorder traversal."""
        result: List[int] = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root: Optional[Node], result: List[int]) -> None:
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.val)
