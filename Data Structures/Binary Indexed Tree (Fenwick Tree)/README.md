# Binary Indexed Tree (Fenwick Tree)

## Introduction

A Binary Indexed Tree, also known as a Fenwick Tree, is a data structure that provides efficient methods for cumulative frequency tables or prefix sums. It allows you to update elements and calculate prefix sums quickly in O(log n) time. It's particularly useful in scenarios involving multiple updates and sum queries on arrays, such as in competitive programming, range query problems, and dynamic cumulative frequency counting.

## Usage

Here is how you can use the `BinaryIndexedTree` class in Python:

# Initialize a Fenwick Tree to support 10 elements
bit = BinaryIndexedTree(10)

# Update the value at position 3 by adding 5
bit.update(3, 5)

# Update the value at position 5 by adding 2
bit.update(5, 2)

# Get prefix sum up to position 5
print(bit.prefix_sum(5))  # Outputs: 7

# Get the sum between indices 3 and 5
print(bit.range_sum(3, 5))  # Outputs: 7

# Get the sum between indices 1 and 2 (no updates done there, so result is 0)
print(bit.range_sum(1, 2))  # Outputs: 0

## Detailed Explanation

The Binary Indexed Tree uses a 1-based indexing array to store cumulative information. The core idea is:

- Update Operation: When you add `delta` at position `index`, you update the `tree` array at all positions that include `index` in their range of prefix sums. This is efficiently done by moving from `index` to `index + (index & -index)` in a loop, leveraging the least significant set bit.

- Prefix Sum Operation: To get the sum of the first `index` elements, you accumulate values from `tree` starting at `index` and move backward by subtracting the least significant set bit (`index -= index & -index`) until you reach zero.

- Range Sum Operation: Computes the sum between two indices `[left, right]` by subtracting the prefix sum up to `left - 1` from the prefix sum up to `right`.

This approach allows both updates and prefix sum queries to run in O(log n) time, where n is the number of elements.

## Complexity Analysis

- Time Complexity:
  - Initialization: O(1)
  - Update: O(log n)
  - Prefix Sum Query: O(log n)
  - Range Sum Query: O(log n)

- Space Complexity:
  - O(n), where n is the number of elements, for storing the Fenwick Tree nodes.

This balance of update and query efficiency makes the Binary Indexed Tree an excellent choice for problems involving dynamic cumulative sums.