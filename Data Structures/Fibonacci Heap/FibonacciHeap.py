class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciHeapNode(key)
        self._merge_with_root_list(node)
        if self.min_node is None or node.key < self.min_node.key:
            self.min_node = node
        self.total_nodes += 1
        return node

    def find_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                children = []
                child = z.child
                while True:
                    children.append(child)
                    child = child.right
                    if child == z.child:
                        break
                for c in children:
                    self._merge_with_root_list(c)
                    c.parent = None

            self._remove_from_root_list(z)

            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()

            self.total_nodes -= 1
            return z.key
        return None

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def union(self, other_heap):
        if not isinstance(other_heap, FibonacciHeap):
            raise ValueError("Can only union with another FibonacciHeap")

        if other_heap.min_node is None:
            return
        if self.min_node is None:
            self.min_node = other_heap.min_node
            self.total_nodes = other_heap.total_nodes
            return

        # Concatenate the root lists
        self._concatenate_root_lists(self.min_node, other_heap.min_node)
        if other_heap.min_node.key < self.min_node.key:
            self.min_node = other_heap.min_node
        self.total_nodes += other_heap.total_nodes

    # --- Internal helper methods --- #

    def _merge_with_root_list(self, node):
        if self.min_node is None:
            node.left = node.right = node
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _concatenate_root_lists(self, a, b):
        a_right = a.right
        b_left = b.left

        a.right = b
        b.left = a

        a_right.left = b_left
        b_left.right = a_right

    def _consolidate(self):
        import math
        max_degree = int(math.log2(self.total_nodes)) + 1 if self.total_nodes > 0 else 0
        A = [None] * max_degree

        root_nodes = []
        current = self.min_node
        if current is not None:
            while True:
                root_nodes.append(current)
                current = current.right
                if current == self.min_node:
                    break

        for w in root_nodes:
            x = w
            d = x.degree
            while d < max_degree and A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._heap_link(y, x)
                A[d] = None
                d += 1
            if d < max_degree:
                A[d] = x

        self.min_node = None
        for i in range(max_degree):
            if A[i] is not None:
                if self.min_node is None or A[i].key < self.min_node.key:
                    self.min_node = A[i]

    def _heap_link(self, y, x):
        self._remove_from_root_list(y)
        y.left = y.right = y
        y.parent = x
        if x.child is None:
            x.child = y
        else:
            y.right = x.child
            y.left = x.child.left
            x.child.left.right = y
            x.child.left = y
        x.degree += 1
        y.mark = False

    def _cut(self, x, y):
        # remove x from child list of y and decrement y.degree
        if y.child == x:
            if x.right != x:
                y.child = x.right
            else:
                y.child = None

        x.left.right = x.right
        x.right.left = x.left
        y.degree -= 1

        # add x to root list
        self._merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)
