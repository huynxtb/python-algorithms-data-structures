# Segment Tree

## Introduction

A Segment Tree is a versatile data structure designed to efficiently perform range queries and updates on an array. It is particularly useful when you need to repeatedly query aggregated data, such as sums, minima, or maxima, over arbitrary segments (intervals) of an array, while also supporting dynamic updates to the array elements. With Segment Trees, these operations can be performed in logarithmic time relative to the size of the array, making it ideal for scenarios where frequent queries and updates are required.

## Usage

Here's an example of how one might use the `SegmentTree` class implemented below:

# Sample array
data = [2, 5, 1, 4, 9, 3]

# Initialize the segment tree
seg_tree = SegmentTree(data)

# Query the sum of elements from index 1 to 4
result = seg_tree.query(1, 4)  # sum of [5, 1, 4, 9]
print(result)  # Output: 19

# Update the element at index 3 to 6
seg_tree.update(3, 6)

# Query again after the update
result = seg_tree.query(1, 4)
print(result)  # Output: 21

## Detailed Explanation

- **Initialization and Building:**
  When the `SegmentTree` is initialized with an input array, it builds a complete binary tree where each node represents the sum of a segment of the array. The leaf nodes correspond to individual elements, while internal nodes store sums of their respective children segments.

- **Structure Representation:**
  The segment tree is stored in a list `tree` where for a node at index `i`:
  - Left child is at `2*i + 1`
  - Right child is at `2*i + 2`
  This allows efficient navigation and reduces overhead compared to pointer-based structures.

- **Query:**
  To compute the sum over a range [left, right], the `_query` method traverses the tree recursively:
  - If the current segment represented by a node is fully within the query range, its stored sum is returned.
  - If the segment is completely outside the query range, it contributes 0.
  - For partial overlaps, the method queries both children and combines their results.

- **Update:**
  To update an element, the `_update` method navigates down to the corresponding leaf node and changes its value. As it unwinds the recursion, it updates the sum values of parent nodes. This maintains the correctness of segment sums after the update.

## Complexity Analysis

- **Time Complexity:**
  - Building the tree takes O(n), where n is the number of elements.
  - Query operations run in O(log n) due to the height of the tree and pruning of non-overlapping segments.
  - Update operations also run in O(log n) since it affects only nodes along the path from the leaf to the root.

- **Space Complexity:**
  - The segment tree requires O(n) space, specifically about 4*n to comfortably store all segments without overflow.

This implementation is clear, efficient, and reusable for any integer array where range sum queries and point updates are needed.