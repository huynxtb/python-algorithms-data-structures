# Counting Sort

## Introduction

Counting Sort is a non-comparative sorting algorithm that sorts integers based on counting the number of occurrences of each distinct value. It is especially efficient when the range of the input values (k) is not significantly larger than the number of elements (n) to be sorted. The algorithm operates in linear time, O(n + k), making it faster than comparison-based sorting algorithms for appropriate data sets. This algorithm only works on non-negative integers as implemented here.

## Usage

from CountingSort import counting_sort

# Example usage:
unsorted_list = [4, 2, 2, 8, 3, 3, 1]
sorted_list = counting_sort(unsorted_list)
print(sorted_list)  # Output: [1, 2, 2, 3, 3, 4, 8]

## Detailed Explanation

1. **Input Validation:** The function handles an empty input list by immediately returning an empty list.
2. **Find Max Value:** It finds the maximum value in the input list to know the range of the counting array.
3. **Initialize Count Array:** It creates a list of zeros, `count`, where each index represents a distinct integer from 0 to the maximum value.
4. **Count Occurrences:** It iterates over the input list, incrementing the count at the index corresponding to each integer.
5. **Build Sorted List:** Finally, it constructs the sorted output by extending a new list with each integer repeated by its recorded count.

## Complexity Analysis

- **Time Complexity:** O(n + k), where n is the number of elements in the input list and k is the range of the input values (max_value).
- **Space Complexity:** O(k) due to the count array, plus O(n) for the output list.

This makes Counting Sort efficient for datasets where k is not substantially larger than n.
