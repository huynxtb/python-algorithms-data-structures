class SegmentTree:
    def __init__(self, data):
        """
        Initialize the Segment Tree with a list of integers.

        :param data: List[int] - The input array for which the segment tree is built.
        """
        self.n = len(data)
        self.tree = [0] * (4 * self.n)  # Allocate enough space for segment tree
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        """
        Recursively build the segment tree.

        :param data: List[int] - The original data array
        :param node: int - Current index in the segment tree array
        :param start: int - Start index of the segment in the original array
        :param end: int - End index of the segment in the original array
        """
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node + 1, start, mid)
            self._build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, value):
        """
        Update the value at a specific index in the original array and
        update the segment tree accordingly.

        :param index: int - The index of the element to update
        :param value: int - The new value to set
        """
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node + 1, start, mid, index, value)
            else:
                self._update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right):
        """
        Query the sum of elements in the range [left, right].

        :param left: int - Start index of the query range
        :param right: int - End index of the query range
        :return: int - Sum of elements in the range
        """
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0  # No overlap
        if left <= start and end <= right:
            return self.tree[node]  # Complete overlap

        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, left, right)
        right_sum = self._query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum
