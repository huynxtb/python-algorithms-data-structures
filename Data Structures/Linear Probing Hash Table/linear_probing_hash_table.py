class LinearProbingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.DELETED = 'DELETED'

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        if self.size / self.capacity > 0.75:
            self._resize()
        index = self._hash(key)
        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity
        self.table[index] = (key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        return None

    def delete(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                self.size -= 1
                return
            index = (index + 1) % self.capacity

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity
        for item in old_table:
            if item is not None and item != self.DELETED:
                self.insert(item[0], item[1])