# Binary Search

## Introduction
Binary Search is a fundamental and widely used algorithm in computer science designed for efficiently searching a target value within a sorted array or list. It works by repeatedly dividing the search interval in half, drastically reducing the number of comparisons needed compared to a linear search. This makes Binary Search particularly valuable when working with large datasets where performance is critical.

## Usage
Suppose you have a sorted list of integers:

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

You want to find the index of the target value 23:

index = binary_search(sorted_list, 23)

print(index)  # Output will be 5, as 23 is at index 5 in the list

If the target is not found, the function returns -1:

missing_index = binary_search(sorted_list, 7)
print(missing_index)  # Output will be -1

## Detailed Explanation
This implementation of Binary Search is iterative (not recursive), making it suitable for environments with limited stack space or where iterative solutions are preferred.

- Two pointers, `left` and `right`, denote the current bounds of the search within the list.
- The middle index `mid` is calculated by safely averaging the `left` and `right` indexes.
- At each iteration:
  - If the element at `mid` matches the target, the search is successful, and the index `mid` is returned.
  - If the element at `mid` is less than the target, the search scope moves to the right half (`left` is updated to `mid + 1`).
  - If the element at `mid` is greater than the target, the search scope moves to the left half (`right` is updated to `mid - 1`).
- The loop continues until `left` is greater than `right`, indicating that the target is not present.

Overall, the binary search efficiently narrows down the location of the target by halving the search space at each step.

## Complexity Analysis
- **Time Complexity:**
  - Best case: O(1) if the target is found at the mid-point initially.
  - Average and worst case: O(log n), where n is the number of elements, due to halving the search space on each iteration.
- **Space Complexity:** O(1) as it uses a fixed amount of extra space regardless of input size.

This efficient search algorithm is ideal for situations requiring frequent search operations in large, sorted datasets.