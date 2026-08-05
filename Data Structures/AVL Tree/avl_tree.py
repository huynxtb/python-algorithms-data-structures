class AVLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, key, val):
        self.root = self._insert(self.root, key, val)

    def _insert(self, node, key, val):
        if not node:
            return AVLNode(key, val)

        if key < node.key:
            node.left = self._insert(node.left, key, val)
        elif key > node.key:
            node.right = self._insert(node.right, key, val)
        else:
            node.val = val
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.val = temp.val
            node.right = self._delete(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self._left_rotate(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node.val if node else None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)