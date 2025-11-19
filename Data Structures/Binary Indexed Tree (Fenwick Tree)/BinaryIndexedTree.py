class BinaryIndexedTree:
    def __init__(self, size):
        """Initialize the Fenwick Tree with a fixed size."""
        self.size = size
        self.tree = [0] * (size + 1)  # 1-based indexing

    def update(self, index, delta):
        """Add delta to element at index (1-based)."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def prefix_sum(self, index):
        """Return the prefix sum from start to index (1-based)."""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & (-index)
        return result

    def range_sum(self, left, right):
        """Return sum of elements between left and right (1-based)."""
        if left > right:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
