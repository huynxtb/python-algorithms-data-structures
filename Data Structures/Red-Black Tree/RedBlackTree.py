class RedBlackNode:
    RED = True
    BLACK = False

    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(key=None, color=RedBlackNode.BLACK)  # Sentinel NIL node
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        node = RedBlackNode(key=key, color=RedBlackNode.RED, left=self.NIL, right=self.NIL, parent=None)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self.insert_fixup(node)

    def insert_fixup(self, z):
        while z.parent.color == RedBlackNode.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RedBlackNode.RED:
                    z.parent.color = RedBlackNode.BLACK
                    y.color = RedBlackNode.BLACK
                    z.parent.parent.color = RedBlackNode.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = RedBlackNode.BLACK
                    z.parent.parent.color = RedBlackNode.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RedBlackNode.RED:
                    z.parent.color = RedBlackNode.BLACK
                    y.color = RedBlackNode.BLACK
                    z.parent.parent.color = RedBlackNode.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = RedBlackNode.BLACK
                    z.parent.parent.color = RedBlackNode.RED
                    self.left_rotate(z.parent.parent)
        self.root.color = RedBlackNode.BLACK

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, key):
        z = self.search_node(self.root, key)
        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == RedBlackNode.BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == RedBlackNode.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RedBlackNode.RED:
                    w.color = RedBlackNode.BLACK
                    x.parent.color = RedBlackNode.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == RedBlackNode.BLACK and w.right.color == RedBlackNode.BLACK:
                    w.color = RedBlackNode.RED
                    x = x.parent
                else:
                    if w.right.color == RedBlackNode.BLACK:
                        w.left.color = RedBlackNode.BLACK
                        w.color = RedBlackNode.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = RedBlackNode.BLACK
                    w.right.color = RedBlackNode.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RedBlackNode.RED:
                    w.color = RedBlackNode.BLACK
                    x.parent.color = RedBlackNode.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == RedBlackNode.BLACK and w.right.color == RedBlackNode.BLACK:
                    w.color = RedBlackNode.RED
                    x = x.parent
                else:
                    if w.left.color == RedBlackNode.BLACK:
                        w.right.color = RedBlackNode.BLACK
                        w.color = RedBlackNode.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = RedBlackNode.BLACK
                    w.left.color = RedBlackNode.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = RedBlackNode.BLACK

    def search_node(self, node, key):
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def search(self, key):
        node = self.search_node(self.root, key)
        if node != self.NIL:
            return node.key
        else:
            return None

    def inorder_helper(self, node, res):
        if node != self.NIL:
            self.inorder_helper(node.left, res)
            res.append(node.key)
            self.inorder_helper(node.right, res)

    def inorder(self):
        res = []
        self.inorder_helper(self.root, res)
        return res
