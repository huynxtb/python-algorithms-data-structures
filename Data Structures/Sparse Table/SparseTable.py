import math
from typing import Generic, TypeVar, Sequence, Callable, List

T = TypeVar('T')

class SparseTable(Generic[T]):
    """
    A Sparse Table is a data structure that can answer range queries (like minimum, maximum, GCD, etc.)
    on a static array in O(1) time after O(N log N) preprocessing.
    It is suitable for idempotent operations, meaning func(x, x) = x.
    Examples of idempotent operations: min, max, GCD, bitwise AND, bitwise OR.
    It is not suitable for sum or count queries, as func(x, x) = x does not hold.
    """

    _data_len: int
    _func: Callable[[T, T], T]
    _st: List[List[T]]
    _log_table: List[int]

    def __init__(self, data: Sequence[T], func: Callable[[T, T], T] = min) -> None:
        """
        Initializes the Sparse Table with the given data and idempotent function.

        Args:
            data: An immutable sequence of elements.
            func: An idempotent binary operation (e.g., min, max, math.gcd).
                  Defaults to `min`.

        Raises:
            ValueError: If the input data is empty.

        Time Complexity: O(N log N) for preprocessing.
        Space Complexity: O(N log N) for storing the lookup table.
        """
        if not data:
            raise ValueError("Input data cannot be empty for SparseTable.")

        self._data_len = len(data)
        self._func = func

        # Precompute floor(log2(i)) for i from 1 to _data_len
        # This allows O(1) lookup for log base 2 without using math.log2 directly in query.
        self._log_table = [0] * (self._data_len + 1)
        for i in range(2, self._data_len + 1):
            self._log_table[i] = self._log_table[i // 2] + 1

        # Determine the maximum power of 2 needed (floor(log2(_data_len)))
        # If _data_len is 1, _max_log is 0.
        _max_log = self._log_table[self._data_len]

        # Initialize the sparse table: _st[k][i] stores the result of func
        # over the range [i, i + 2^k - 1]
        # The type ignore is used because `None` is not strictly `T`, but it's immediately
        # overwritten with actual `T` values during initialization.
        self._st = [[None] * self._data_len for _ in range(_max_log + 1)] # type: ignore

        # Base case: k = 0, each segment is of length 2^0 = 1
        for i in range(self._data_len):
            self._st[0][i] = data[i]

        # Fill the sparse table for k from 1 to _max_log
        # Each segment of length 2^k is formed by combining two segments of length 2^(k-1)
        for k in range(1, _max_log + 1):
            for i in range(self._data_len - (1 << k) + 1):
                self._st[k][i] = self._func(
                    self._st[k - 1][i],
                    self._st[k - 1][i + (1 << (k - 1))]
                )

    def query(self, left: int, right: int) -> T:
        """
        Computes the range query over the inclusive interval [left, right].

        Args:
            left: The starting index of the range (inclusive).
            right: The ending index of the range (inclusive).

        Returns:
            The result of applying the idempotent function over the specified range.

        Raises:
            IndexError: If `left` or `right` are out of bounds.
            ValueError: If `left` is greater than `right`.

        Time Complexity: O(1).
        """
        if not (0 <= left < self._data_len and 0 <= right < self._data_len):
            raise IndexError(f"Indices ({left}, {right}) out of bounds for data of length {self._data_len}.")
        if left > right:
            raise ValueError(f"Left index ({left}) cannot be greater than right index ({right}).")

        # Determine the largest power of 2, k, such that 2^k <= (right - left + 1)
        k = self._log_table[right - left + 1]

        # The range [left, right] is covered by two overlapping segments of length 2^k:
        # 1. [left, left + 2^k - 1]
        # 2. [right - 2^k + 1, right]
        # Since the operation is idempotent, the overlap doesn't affect the result.
        return self._func(
            self._st[k][left],
            self._st[k][right - (1 << k) + 1]
        )

    def __len__(self) -> int:
        """
        Returns the number of elements in the underlying data array.

        Time Complexity: O(1).
        """
        return self._data_len
