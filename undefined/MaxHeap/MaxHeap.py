class MaxHeap:
    def __init__(self):
        self._heap = []

    def insert(self, key):
        self._heap.append(key)
        self._sift_up(len(self._heap) - 1)

    def extract_max(self):
        if not self._heap:
            raise IndexError("extract_max() called on empty heap")
        max_elem = self._heap[0]
        last_elem = self._heap.pop()
        if self._heap:
            self._heap[0] = last_elem
            self._sift_down(0)
        return max_elem

    def peek_max(self):
        if not self._heap:
            raise IndexError("peek_max() called on empty heap")
        return self._heap[0]

    def heapify(self, array):
        self._heap = array[:]
        start = (len(self._heap) - 2) // 2
        for i in range(start, -1, -1):
            self._sift_down(i)

    def size(self):
        return len(self._heap)

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self._heap[idx] > self._heap[parent]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        size = len(self._heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < size and self._heap[left] > self._heap[largest]:
                largest = left
            if right < size and self._heap[right] > self._heap[largest]:
                largest = right
            if largest == idx:
                break
            self._heap[idx], self._heap[largest] = self._heap[largest], self._heap[idx]
            idx = largest
