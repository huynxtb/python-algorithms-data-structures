class UnionFind:
    def __init__(self, n):
        # Initialize each element to be its own parent (self root)
        self.parent = list(range(n))
        # Initialize the size of each set to 1
        self.size = [1] * n

    def find(self, x):
        # Find the root of the set containing x with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union the sets containing x and y using union by size
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Attach smaller tree under the larger tree root
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

    def connected(self, x, y):
        # Check if x and y have the same root
        return self.find(x) == self.find(y)