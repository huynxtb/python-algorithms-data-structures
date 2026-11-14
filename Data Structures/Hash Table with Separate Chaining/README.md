# Hash Table with Separate Chaining

## Introduction
A Hash Table is a data structure that implements an associative array, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. This implementation uses separate chaining to handle collisions, where each bucket contains a list of entries that hash to the same index.

## Usage

hash_table = HashTable()
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'
print(hash_table['key1'])  # Output: value1
del hash_table['key2']
print('key2' in hash_table)  # Output: False
print(len(hash_table))  # Output: 1


## Detailed Explanation
The `HashTable` class initializes with a specified capacity and a load factor threshold. The `_hash_function` method computes the index for a given key. The `__setitem__` method allows adding or updating key-value pairs, while `__getitem__` retrieves values. The `__delitem__` method removes entries, and `__contains__` checks for key existence. The `_resize` method is called when the load factor exceeds the threshold, doubling the capacity and rehashing existing entries.

## Complexity Analysis
- **Insertion (Average Case):** O(1)
- **Retrieval (Average Case):** O(1)
- **Deletion (Average Case):** O(1)
- **Space Complexity:** O(n) where n is the number of key-value pairs stored.