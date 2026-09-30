# Sparse Table

## 1. Introduction

The Sparse Table is a powerful data structure designed for efficiently answering Range Minimum/Maximum Queries (RMQ) and other general idempotent range queries on a static array. Once built, it can answer queries in `O(1)` time, making it highly suitable for scenarios where the underlying data does not change, but many queries need to be performed.

An operation is considered **idempotent** if applying it multiple times to the same value yields the same result (e.g., `func(x, x) = x`). Examples of idempotent operations include `min`, `max`, `math.gcd`, bitwise AND (`&`), and bitwise OR (`|`). The Sparse Table is not suitable for non-idempotent operations like sum or count, as overlapping segments would lead to incorrect results.

## 2. Usage

To use the `SparseTable`, you initialize it with a sequence of data and an optional idempotent binary function. If no function is provided, it defaults to `min`.


import math

# Example 1: Range Minimum Query (RMQ)
data_min = [2, 4, 3, 1, 6, 7, 8, 9, 1]
st_min = SparseTable(data_min, func=min)
# Query minimum in [0, 4] -> min(2, 4, 3, 1, 6) = 1
result_min = st_min.query(0, 4) # Expected: 1
print(f"Min in [0, 4]: {result_min}")
# Query minimum in [5, 8] -> min(7, 8, 9, 1) = 1
result_min_2 = st_min.query(5, 8) # Expected: 1
print(f"Min in [5, 8]: {result_min_2}")

# Example 2: Range Maximum Query (RMQ)
data_max = [2, 4, 3, 1, 6, 7, 8, 9, 1]
st_max = SparseTable(data_max, func=max)
# Query maximum in [0, 4] -> max(2, 4, 3, 1, 6) = 6
result_max = st_max.query(0, 4) # Expected: 6
print(f"Max in [0, 4]: {result_max}")

# Example 3: Range GCD Query
data_gcd = [12, 18, 6, 30, 15, 9]
st_gcd = SparseTable(data_gcd, func=math.gcd)
# Query GCD in [0, 2] -> gcd(12, 18, 6) = 6
result_gcd = st_gcd.query(0, 2) # Expected: 6
print(f"GCD in [0, 2]: {result_gcd}")
# Query GCD in [2, 5] -> gcd(6, 30, 15, 9) = 3
result_gcd_2 = st_gcd.query(2, 5) # Expected: 3
print(f"GCD in [2, 5]: {result_gcd_2}")

# Example 4: Length of the underlying data
data_len_example = [1, 2, 3]
st_len = SparseTable(data_len_example)
length = len(st_len) # Expected: 3
print(f"Length of SparseTable: {length}")

# Example 5: Handling invalid queries
try:
    st_min.query(-1, 2)
except IndexError as e:
    print(f"Error: {e}")
try:
    st_min.query(5, 2)
except ValueError as e:
    print(f"Error: {e}")


## 3. Detailed Explanation

The Sparse Table works by precomputing the results of the idempotent operation for all possible segment lengths that are powers of two. This precomputed information is stored in a 2D array, `_st`.

### Preprocessing (`__init__`)

1.  **`_log_table` Precomputation**: An auxiliary array `_log_table` is created to store `floor(log2(i))` for each `i` from 1 to `N` (where `N` is the length of the input data). This allows for `O(1)` lookup of the largest power of two less than or equal to a given range length, without relying on `math.log2` during queries.
    The calculation `_log_table[i] = _log_table[i // 2] + 1` efficiently computes these values.

2.  **`_st` Table Initialization**: The main sparse table `_st` is a 2D list where `_st[k][i]` stores the result of applying the `_func` operation over the segment `data[i ... i + 2^k - 1]`. The table has `log N + 1` rows (for `k` from 0 to `floor(log2(N))`) and `N` columns.

3.  **Base Case (k=0)**: The first row (`k=0`) of `_st` is initialized directly from the input `data`. `_st[0][i]` simply stores `data[i]`, representing segments of length `2^0 = 1`.

4.  **Filling the Table (k > 0)**: For each subsequent row `k` (from 1 up to `floor(log2(N))`), `_st[k][i]` is computed by combining two segments of length `2^(k-1)`:
    *   The first segment starts at `i`: `_st[k-1][i]` covers `data[i ... i + 2^(k-1) - 1]`. 
    *   The second segment starts at `i + 2^(k-1)`: `_st[k-1][i + (1 << (k-1))]` covers `data[i + 2^(k-1) ... i + 2^k - 1]`. 
    The `_func` is applied to these two results: `_st[k][i] = _func(_st[k-1][i], _st[k-1][i + (1 << (k-1))])`. This process fills the entire table.

### Querying (`query`)

1.  **Bounds Checking**: The `query` method first validates the `left` and `right` indices to ensure they are within the bounds of the original data and that `left <= right`.

2.  **Determining `k`**: For a given query range `[left, right]`, the length of the range is `length = right - left + 1`. The largest power of two, `2^k`, that is less than or equal to `length` is determined using the precomputed `_log_table`: `k = _log_table[length]`.

3.  **Combining Segments**: The key insight for `O(1)` query time with idempotent operations is that any range `[left, right]` can be covered by at most two overlapping segments of length `2^k`. Specifically, these two segments are:
    *   `_st[k][left]`: Covers the range `[left, left + 2^k - 1]`. 
    *   `_st[k][right - (1 << k) + 1]`: Covers the range `[right - 2^k + 1, right]`. 
    Since the operation is idempotent, applying `_func` to the results of these two overlapping segments correctly yields the result for the entire `[left, right]` range, as the overlap does not introduce errors.

## 4. Complexity Analysis

### Time Complexity

*   **`__init__(self, data, func)`**: `O(N log N)`
    *   The `_log_table` precomputation takes `O(N)` time.
    *   The nested loops for filling the `_st` table iterate `log N` times for `k` and `N` times for `i`, resulting in `O(N log N)`.
*   **`query(self, left, right)`**: `O(1)`
    *   Retrieving `k` from `_log_table` is `O(1)`.
    *   Accessing two elements from `_st` and applying `_func` is `O(1)`.
*   **`__len__(self)`**: `O(1)`

### Space Complexity

*   **`__init__(self, data, func)`**: `O(N log N)`
    *   The `_st` table stores `N * (log N + 1)` elements, leading to `O(N log N)` space.
    *   The `_log_table` stores `N + 1` elements, leading to `O(N)` space.
