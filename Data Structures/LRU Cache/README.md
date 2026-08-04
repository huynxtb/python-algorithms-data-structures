# Introduction
The LRU Cache, or Least Recently Used Cache, is a type of cache where the least recently used items are discarded first when the cache reaches its capacity. This data structure is particularly useful in scenarios where memory or storage is limited, and the most recently accessed items are likely to be accessed again in the near future.

# Usage

from LRUCache import LRUCache

cache = LRUCache(2)

cache.put(1, 1)

cache.put(2, 2)

print(cache.get(1))  # returns 1

cache.put(3, 3)  # evicts key 2

print(cache.get(2))  # returns -1 (not found)

cache.put(4, 4)  # evicts key 1

print(cache.get(1))  # returns -1 (not found)

cache.get(3)  # returns 3

cache.get(4)  # returns 4


# Detailed Explanation
The implementation uses an `OrderedDict` from the `collections` module to maintain the order of the keys based on their last access time. The `get` method checks if the key is present in the cache, and if so, it moves the key to the end of the ordered dictionary to mark it as recently used. The `put` method checks if the key is already present in the cache, and if so, it updates the value and moves the key to the end. If the key is not present and the cache is full, it removes the least recently used item (the first item in the ordered dictionary) before adding the new key-value pair.

# Complexity Analysis
* Time complexity for `get` and `put` operations: O(1)
* Space complexity: O(capacity), where capacity is the maximum number of items the cache can hold