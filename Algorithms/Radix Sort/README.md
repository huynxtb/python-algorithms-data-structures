# Radix Sort (LSD) in Python

## 1. Introduction

Radix Sort is a non-comparative integer sorting algorithm that sorts numbers by processing individual digits. The Least Significant Digit (LSD) variant processes digits starting from the least significant digit to the most significant digit. Radix Sort is especially useful when sorting integers with fixed digit length or when the keys are integers or strings with a bounded length. It is often efficient for large lists of integers as its time complexity can be better than comparison-based algorithms in many cases.


## 2. Usage

A basic example:

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_numbers = radix_sort(numbers)
print(sorted_numbers)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]

The `radix_sort` function does not modify the original list and returns a new sorted list.


## 3. Detailed Explanation

- The main function `radix_sort` first finds the maximum number in the input list to determine the number of digits it needs to process.
- It iterates through each digit position starting from the least significant digit (units place), moving to tens, hundreds, and so forth.
- For each digit position represented by `exp` (1, 10, 100...), it calls a helper function `_counting_sort_by_digit`.
- `_counting_sort_by_digit` performs a stable counting sort based on the digit at the current position:
  - It counts the occurrences of each digit (0-9) at that position.
  - Converts counts to positions by cumulative sum.
  - Builds the output array by placing elements in their correct sorted positions by digit, iterating backwards to keep stability.
- After all digit positions are processed, the output list is fully sorted.
- The stability of counting sort ensures that sorting by less significant digits does not disrupt the order of the previously sorted more significant digits.


## 4. Complexity Analysis

- **Time Complexity:**
  - Let n be the number of elements, and d be the number of digits in the maximum element.
  - Each digit requires a counting sort, which is O(n + k) where k is the base (10).
  - Total complexity: O(d * (n + k)) which simplifies to O(d * n) since k=10 is constant.
  - For numbers with fixed digit length, this is effectively linear time.

- **Space Complexity:**
  - Additional arrays for counting and output use O(n + k) space.
  - Overall space complexity is O(n).

This makes LSD Radix Sort practical and efficient for sorting large lists of fixed-length integers.