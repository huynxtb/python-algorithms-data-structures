# Counting Bloom Filter

## Introduction

The Counting Bloom Filter is a probabilistic data structure that extends the classic Bloom Filter by enabling removal of items. Unlike the traditional Bloom Filter, which uses bits to indicate presence of elements, the Counting Bloom Filter maintains an internal array of integer counters to allow decrementing counts when items are removed. It is useful for applications where membership tests with false positive rates are acceptable, but the ability to delete elements from the filter is required.

## Usage

# Initialize a counting bloom filter with size 1000 counters and 4 hash functions
cbf = CountingBloomFilter(size=1000, hash_count=4)

# Add an item
cbf.add("apple")

# Check membership
if cbf.contains("apple"):
    print("apple might be in the set")
else:
    print("apple is definitely not in the set")

# Remove an item
cbf.remove("apple")

# After removal
if cbf.contains("apple"):
    print("apple might be in the set")
else:
    print("apple is definitely not in the set")

## Detailed Explanation

- **Initialization:** The filter is created with a specified size and number of hash functions. Internally, it keeps an array of counters initialized to zero.

- **Hashing:** Two cryptographic hash functions (`md5` and `sha1`) are used to produce two base hash values for an item. These are combined in a double hashing technique to simulate multiple different hash functions, avoiding the cost of many independent hashes.

- **Adding an Item:** Each hash function computes an index into the counting array. The value at each of these indices is incremented by one.

- **Removing an Item:** Similar to adding, each hash function computes indices and the corresponding counters are decremented, but never below zero to prevent underflow.

- **Membership Test:** To check if an item is in the filter, all counters at the indices determined by the hash functions must be greater than zero. If any are zero, the item is definitely not present.

This structure allows for approximate membership testing with the ability to remove items, though it may yield false positives but no false negatives.

## Complexity Analysis

- **Time Complexity:**
  - `add(item)`: O(k), where k is the number of hash functions.
  - `remove(item)`: O(k).
  - `contains(item)`: O(k).

- **Space Complexity:**
  - O(m), where m is the size of the counting array.

This efficiency makes Counting Bloom Filter suited for high-performance systems that require insertions, queries, and deletions with minimal memory footprint and acceptable error rates.