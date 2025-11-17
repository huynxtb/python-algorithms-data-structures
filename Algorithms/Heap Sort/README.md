# Heap Sort

## Introduction
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements efficiently. It has a guaranteed time complexity of O(n log n) in all cases and is particularly useful when a stable and efficient sorting algorithm is required without additional memory allocation, since it operates in-place.

## Usage
Example usage of heap_sort function:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]

## Detailed Explanation
The implementation consists of three main functions:

1. heapify(arr, n, i):
   - Maintains the max-heap property for a subtree rooted at index i, assuming the subtrees are already heaps.
   - Compares the root with its left and right children and swaps if necessary.
   - If a swap is performed, recursively heapifies the affected subtree.

2. build_max_heap(arr):
   - Converts the input array into a max heap by calling heapify on all internal nodes from the bottom up.

3. heap_sort(arr):
   - Builds a max heap.
   - Repeatedly swaps the root with the last element and reduces heap size.
   - Calls heapify on the reduced heap to maintain max heap property.

## Complexity Analysis
- Time Complexity: O(n log n)
- Space Complexity: O(1) (in-place)

This implementation uses only functions and no runtime or input/output code.