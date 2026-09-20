from typing import List, Tuple


class Manacher:
    """
    A production-grade implementation of Manacher's Algorithm for finding
    palindromic substrings in linear time O(n) and answering range palindrome
    queries in O(1) time.
    """

    def __init__(self, text: str) -> None:
        """
        Initializes the Manacher data structure with the given text and
        precomputes the palindrome radius array in O(n) time.

        Args:
            text (str): The input string to process.
        """
        self._text: str = text
        self._n: int = len(text)
        self._transformed: str = ""
        self._radii: List[int] = []
        self._preprocess_and_compute()

    def _preprocess_and_compute(self) -> None:
        """
        Transforms the input string by inserting boundary sentinels and delimiters,
        then computes the palindrome radii using Manacher's Algorithm.
        """
        if not self._text:
            return

        # Transform text: "abc" -> "^#a#b#c#$"
        # '^' and '$' are sentinels to avoid bounds checking.
        chars: List[str] = ["^"]
        for char in self._text:
            chars.append("#")
            chars.append(char)
        chars.append("#")
        chars.append("$")
        self._transformed = "".join(chars)

        m = len(self._transformed)
        self._radii = [0] * m
        center = 0
        right = 0

        for i in range(1, m - 1):
            mirror = 2 * center - i

            if i < right:
                self._radii[i] = min(right - i, self._radii[mirror])

            # Attempt to expand palindrome centered at i
            while self._transformed[i + 1 + self._radii[i]] == self._transformed[i - 1 - self._radii[i]]:
                self._radii[i] += 1

            # Update center and right boundary if expanded beyond right
            if i + self._radii[i] > right:
                center = i
                right = i + self._radii[i]

    def longest_palindromic_substring(self) -> str:
        """
        Returns the longest contiguous palindromic substring in the original text.

        Returns:
            str: The longest palindromic substring. Returns an empty string if
                 the input text is empty.
        """
        if not self._text:
            return ""

        max_len = 0
        center_idx = 0
        for i in range(1, len(self._radii) - 1):
            if self._radii[i] > max_len:
                max_len = self._radii[i]
                center_idx = i

        start_idx = (center_idx - max_len) // 2
        return self._text[start_idx:start_idx + max_len]

    def is_palindrome(self, start: int, end: int) -> bool:
        """
        Checks whether the substring text[start:end+1] is a palindrome in O(1) time.

        Args:
            start (int): The 0-based inclusive starting index.
            end (int): The 0-based inclusive ending index.

        Returns:
            bool: True if text[start:end+1] is a palindrome, False otherwise.

        Raises:
            IndexError: If start or end are out of valid string bounds.
            ValueError: If start > end.
        """
        if start < 0 or end >= self._n:
            raise IndexError("Indices out of string bounds.")
        if start > end:
            raise ValueError("start index must be less than or equal to end index.")

        # Map original string indices to transformed string indices
        # Original index k maps to transformed index 2 * k + 2
        trans_start = 2 * start + 2
        trans_end = 2 * end + 2
        trans_center = (trans_start + trans_end) // 2
        expected_radius = (trans_end - trans_start) // 2

        return self._radii[trans_center] >= expected_radius

    def count_palindromic_substrings(self) -> int:
        """
        Counts the total number of palindromic substring occurrences in the string.

        Returns:
            int: Total number of palindromic substrings.
        """
        if not self._text:
            return 0

        total_count = 0
        for radius in self._radii:
            total_count += (radius + 1) // 2
        return total_count

    def all_longest_palindromes(self) -> List[Tuple[int, int]]:
        """
        Returns a list of (start_index, end_index) tuples (0-indexed, inclusive)
        for all maximal palindromes centered at every possible character and
        inter-character boundary.

        Returns:
            List[Tuple[int, int]]: List of (start, end) tuples representing all
                                   maximal palindromic substrings.
        """
        if not self._text:
            return []

        maximal_palindromes: List[Tuple[int, int]] = []
        for i in range(1, len(self._radii) - 1):
            radius = self._radii[i]
            if radius > 0:
                start = (i - radius) // 2
                end = start + radius - 1
                maximal_palindromes.append((start, end))
        return maximal_palindromes
