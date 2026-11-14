class HashTable:
    def __init__(self, initial_capacity=101, load_factor_threshold=0.7):
        self._capacity = initial_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        self._load_factor_threshold = load_factor_threshold

    def _hash_function(self, key):
        return hash(key) % self._capacity

    def __setitem__(self, key, value):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self._buckets[index]):
            if k == key:
                self._buckets[index][i] = (key, value)
                return
        self._buckets[index].append((key, value))
        self._size += 1
        if self._size / self._capacity > self._load_factor_threshold:
            self._resize()

    def __getitem__(self, key):
        index = self._hash_function(key)
        for k, v in self._buckets[index]:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self._buckets[index]):
            if k == key:
                del self._buckets[index][i]
                self._size -= 1
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        index = self._hash_function(key)
        for k, v in self._buckets[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self._size

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value
