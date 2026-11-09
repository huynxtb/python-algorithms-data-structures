# Shell Sort

## Introduction
Shell Sort is an efficient sorting algorithm that generalizes insertion sort to allow the exchange of items that are far apart. The algorithm uses a gap sequence to arrange elements in a way that allows for more efficient sorting than simple insertion sort. It is particularly useful for medium-sized arrays and is a good choice when memory usage is a concern.

## Usage
Here is an example of how to use the `shell_sort` function:

unsorted_list = [12, 34, 54, 2, 3]
sorted_list = shell_sort(unsorted_list)
print(sorted_list)  # Output: [2, 3, 12, 34, 54]


## Detailed Explanation
The `shell_sort` function begins by determining the length of the input array. It initializes a gap value, starting at half the length of the array. The algorithm then performs a gapped insertion sort, where elements are compared and swapped based on the current gap. After each pass, the gap is reduced, allowing for finer sorting until the gap is zero, at which point the array is fully sorted. This method reduces the number of inversions and improves the efficiency of the sorting process compared to standard insertion sort.

## Complexity Analysis
- **Time Complexity:** The average and worst-case time complexity of Shell Sort can vary based on the gap sequence used, but it is generally between O(n log n) and O(n^2). The best-case time complexity is O(n) when the array is already sorted.
- **Space Complexity:** The space complexity is O(1) since it is an in-place sorting algorithm, requiring only a constant amount of additional space.