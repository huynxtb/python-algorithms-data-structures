# Suffix Array

## Introduction
A suffix array is a data structure that stores the starting indices of all suffixes of a string in lexicographical order. It is widely used in string processing and searching problems such as substring search, pattern matching, string comparisons, and in bioinformatics for DNA analysis. Building a suffix array efficiently enables fast queries on the string substrings.

This implementation provides a reusable Python class `SuffixArray` that, given an input string, constructs the suffix array using an efficient O(n log n) algorithm based on sorting suffixes by their first 2^k characters iteratively.

## Usage

from SuffixArray import SuffixArray

text = "banana"
suff_arr = SuffixArray(text)

# Access the suffix array
print(suff_arr.get_suffix_array())  # Output: [5, 3, 1, 0, 4, 2]

# Compare suffixes at positions 1 and 4
result = suff_arr.compare_suffixes(1, 4)
print(result)  # Negative if suffix at 1 < suffix at 4

## Detailed Explanation
- The suffix array is built by initially ranking each suffix by its first character numeric value.
- Using a doubling technique, the algorithm sorts suffixes based on first 2^k characters, for k = 0, 1, 2, ..., until 2^k >= n.
- Sorting is performed using Python's built-in sort with a custom key derived from current rankings.
- After sorting, new ranks are assigned to suffixes; if two suffixes differ, they get different ranks.
- This process efficiently produces the suffix array in O(n log n) time.

The method `compare_suffixes(i, j)` compares two suffixes lexicographically by directly comparing characters until a difference or end is reached.

## Complexity Analysis
- Time Complexity:
  - Construction: O(n log n) due to sorting phases doubling k each iteration.
  - Suffix comparison: O(n) in worst case (comparing suffixes character by character).
- Space Complexity: O(n) for storing the suffix array and rank arrays.

This implementation is self-contained, requires no external dependencies, and can be imported directly for use in string algorithm applications.