# Linear Probing Hash Table

## Introduction
The Linear Probing Hash Table is a data structure that implements a hash table using linear probing to resolve collisions. It is useful when you need an efficient way to store and retrieve key-value pairs, especially when the number of entries is not known in advance.

## Usage

hash_table = LinearProbingHashTable()
hash_table.insert('key1', 'value1')
hash_table.insert('key2', 'value2')
print(hash_table.get('key1'))  # Output: value1
hash_table.delete('key1')
print(hash_table.get('key1'))  # Output: None


## Detailed Explanation
The implementation consists of a class `LinearProbingHashTable` that initializes a hash table with a specified capacity. The `_hash` method computes the index for a given key using a modulo operation. The `insert` method adds a key-value pair, handling collisions through linear probing. The `get` method retrieves the value for a given key, and the `delete` method marks a key as deleted using a sentinel value. The table automatically resizes when the load factor exceeds 0.75, ensuring efficient space utilization.

## Complexity Analysis
- **Insert:** Average O(1), Worst O(n) (due to resizing)
- **Get:** Average O(1), Worst O(n)
- **Delete:** Average O(1), Worst O(n)
- **Space Complexity:** O(n) where n is the number of elements in the hash table.