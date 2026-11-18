# Introduction
The Median of Medians algorithm is a selection algorithm that finds the k-th smallest element in an unsorted list. It is particularly useful when you need a guaranteed worst-case time complexity of O(n), making it more efficient than simpler algorithms like Quickselect in certain scenarios.

# Usage

mom = MedianOfMedians()
result = mom.select([3, 1, 2, 5, 4], 2)  # Finds the 3rd smallest element (0-indexed)
print(result)  # Output: 3


# Detailed Explanation
The algorithm works by dividing the input list into sublists of at most 5 elements each. It computes the median of each sublist and then recursively finds the median of these medians. This median is used as a pivot to partition the original list into elements less than and greater than the pivot. Depending on the value of k, the algorithm continues searching in the appropriate partition until it finds the k-th smallest element.

# Complexity Analysis
- **Time Complexity:** O(n) in the worst case due to the partitioning and recursive selection of the median of medians.
- **Space Complexity:** O(n) for storing the sublists and partitions.