# Exponential Search

## 1. Introduction

Exponential Search is an algorithm designed to search for a target value in a **sorted array**. It is particularly efficient when the target element is located near the beginning of the array, or when the array is unbounded (infinite). The algorithm combines two well-known techniques:

1.  **Exponential Range Finding:** It first finds a range `[low, high]` where the target *might* exist by checking elements at indices `1, 2, 4, 8, 16, ...` (powers of 2) until an element greater than the target is found or the array boundary is exceeded.
2.  **Binary Search:** It then performs a standard binary search within the identified range to pinpoint the exact index of the target.

**When to use it:**
- When you are dealing with a sorted array and the target is likely near the start.
- When working with unbounded or very large sorted arrays where the size is unknown.
- As a practical alternative to binary search when the position of the target is not uniformly distributed.

---

## 2. Usage


# Import or include the functions in your script
# (binary_search and exponential_search)

# Example 1: Target is present in the array
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 7

result = exponential_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index: {result}")
else:
    print(f"Target {target_value} not found in the array.")
# Output: Target 7 found at index: 3


# Example 2: Target is NOT present in the array
target_value_2 = 6

result_2 = exponential_search(sorted_array, target_value_2)

if result_2 != -1:
    print(f"Target {target_value_2} found at index: {result_2}")
else:
    print(f"Target {target_value_2} not found in the array.")
# Output: Target 6 not found in the array.


# Example 3: Empty array
empty_array = []
result_3 = exponential_search(empty_array, 5)
print(f"Result for empty array: {result_3}")
# Output: Result for empty array: -1


# Example 4: Target at the first position
result_4 = exponential_search(sorted_array, 1)
print(f"Target 1 found at index: {result_4}")
# Output: Target 1 found at index: 0


---

## 3. Detailed Explanation

The implementation consists of two functions:

### `exponential_search(arr, target)`

This is the main entry point for the algorithm.

1.  **Edge Case - Empty Array:** If the array has no elements, it immediately returns `-1`.
2.  **Edge Case - First Element:** It checks if the target is at index `0`. If so, it returns `0` immediately, avoiding the loop logic.
3.  **Phase 1 - Exponential Range Finding:**
    - An `index` variable starts at `1`.
    - A `while` loop runs as long as `index` is within the array bounds (`index < n`) AND the element at `arr[index]` is less than or equal to the `target`.
    - In each iteration, `index` is doubled (`index *= 2`). This is the "exponential" part of the algorithm.
    - The loop terminates when `arr[index] > target` (we've overshot) or `index >= n` (we've gone out of bounds).
4.  **Phase 2 - Binary Search:**
    - After the loop, the target (if it exists) must be in the range `[index // 2, min(index, n - 1)]`.
    - `index // 2` is the last index where `arr[index] <= target` was true.
    - `min(index, n - 1)` caps the right boundary to the last valid index.
    - The helper `binary_search` function is called with these boundaries.

### `binary_search(arr, left, right, target)`

This is a standard iterative binary search.

1.  It calculates the `mid` index using `left + (right - left) // 2` to prevent integer overflow (a best practice).
2.  If `arr[mid] == target`, the index is returned.
3.  If `arr[mid] < target`, the search continues in the right half (`left = mid + 1`).
4.  If `arr[mid] > target`, the search continues in the left half (`right = mid - 1`).
5.  If the loop ends without finding the target, `-1` is returned.

---

## 4. Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| **Search (target found)** | O(log i) | O(1) |
| **Search (target not found)** | O(log n) | O(1) |
| **Overall** | O(log n) | O(1) |

**Explanation:**

- **Time Complexity:**
  - The **exponential phase** takes `O(log i)` time, where `i` is the index of the target element. It takes `log i` steps to find the range `[i/2, i]`.
  - The **binary search phase** operates on a range of size `i/2`, which also takes `O(log i)` time.
  - Therefore, the overall time complexity is **O(log i)**. In the worst case (target at the end or not present), `i` approaches `n`, making it **O(log n)**.
  - This is better than a standard binary search (`O(log n)`) when the target is near the beginning of the array.

- **Space Complexity:**
  - The algorithm uses only a constant amount of extra space for variables (`index`, `left`, `right`, `mid`). No additional data structures are used.
  - Therefore, the space complexity is **O(1)**.