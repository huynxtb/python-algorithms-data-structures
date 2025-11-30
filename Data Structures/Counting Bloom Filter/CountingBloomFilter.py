import hashlib

class CountingBloomFilter:
    def __init__(self, size: int, hash_count: int):
        """
        Initialize the Counting Bloom Filter.
        :param size: The size of the counting array.
        :param hash_count: The number of hash functions to use.
        """
        self.size = size
        self.hash_count = hash_count
        self.counts = [0] * size

    def _hashes(self, item):
        """
        Generate a list of hash values for the item, each corresponding to a position in the counting array.
        Uses double hashing technique (two hashes combined) to generate multiple hashes.
        :param item: The item to hash.
        :return: A list of indices.
        """
        item_bytes = str(item).encode('utf-8')
        hash1 = int(hashlib.md5(item_bytes).hexdigest(), 16)
        hash2 = int(hashlib.sha1(item_bytes).hexdigest(), 16)

        for i in range(self.hash_count):
            # Use double hashing to simulate multiple hash functions
            combined_hash = (hash1 + i * hash2) % self.size
            yield combined_hash

    def add(self, item):
        """
        Add an item to the filter.
        """
        for idx in self._hashes(item):
            self.counts[idx] += 1

    def remove(self, item):
        """
        Remove an item from the filter by decrementing the counters where the item hashes.
        If the item does not exist, counters will not go below zero.
        """
        for idx in self._hashes(item):
            if self.counts[idx] > 0:
                self.counts[idx] -= 1

    def contains(self, item) -> bool:
        """
        Check if an item is possibly in the filter.
        Returns True if the item might be in the filter (no false negatives),
        False if the item is definitely not in the filter.
        """
        return all(self.counts[idx] > 0 for idx in self._hashes(item))
