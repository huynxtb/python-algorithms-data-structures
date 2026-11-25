class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError('extract_min() called on empty heap')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek_min(self):
        if self.is_empty():
            raise IndexError('peek_min() called on empty heap')
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        parent_index = self._get_parent_index(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        return 2 * index + 1

    def _get_right_child_index(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]