# Manacher's Algorithm

## 1. Introduction
Manacher's Algorithm is an optimal, linear-time algorithm designed to find all maximal palindromic substrings in a given string. Naive approaches to finding palindromes or the longest palindromic substring check centers with outward expansion in $O(n^2)$ time. Manacher's algorithm utilizes previously computed palindrome symmetries to avoid redundant character comparisons, reducing the overall time complexity to strictly $O(n)$.

Common applications include:
- Finding the longest palindromic substring.
- Answering range palindrome queries in $O(1)$ constant time.
- Counting all distinct occurrences of palindromic substrings in linear time.
- Bioinformatics analysis for palindromic DNA/RNA sequences.

## 2. Usage


from manacher import Manacher

# Initialize Manacher data structure
text = "abacaba"
solver = Manacher(text)

# 1. Get the longest palindromic substring
longest = solver.longest_palindromic_substring()
# Output: "abacaba"

# 2. Check if a substring text[start:end+1] is a palindrome in O(1)
is_pal = solver.is_palindrome(0, 2)  # "aba"
# Output: True

is_pal_sub = solver.is_palindrome(1, 3)  # "bac"
# Output: False

# 3. Count total palindromic substring occurrences
total = solver.count_palindromic_substrings()
# Output: 12

# 4. Get (start, end) bounds for all maximal palindromes
maximal_ranges = solver.all_longest_palindromes()


## 3. Detailed Explanation
1. **Transformation:** The original string of length $n$ is transformed into a string of length $2n + 3$ by interleaving `#` delimiters and adding unique boundary sentinels (e.g., `^` at the beginning and `$` at the end). This allows odd-length and even-length palindromes to be processed uniformly without parity branching or out-of-bounds errors.
2. **Radius Array and Symmetry Exploitation:** An array `radii` stores the palindrome radius around each center. A tracking pointer `center` and rightmost boundary `right` maintain the extent of the furthest-reaching palindrome discovered so far. For any position $i < right$, its initial radius is initialized to $\min(right - i, radii[2 \cdot center - i])$.
3. **Expansion & Center Shift:** The algorithm expands outward from index $i$ only when needed. If the expanded palindrome exceeds `right`, the `center` and `right` markers are updated accordingly.
4. **Constant-Time Queries:** Range verification `is_palindrome(start, end)` maps original substring indices to transformed coordinates and checks whether the precomputed radius at the transformed center is at least half the length of the query range.

## 4. Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| **Initialization (`__init__`)** | $O(n)$ | $O(n)$ |
| **`longest_palindromic_substring`** | $O(n)$ | $O(n)$ (for substring creation) |
| **`is_palindrome`** | $O(1)$ | $O(1)$ |
| **`count_palindromic_substrings`** | $O(n)$ | $O(1)$ |
| **`all_longest_palindromes`** | $O(n)$ | $O(n)$ |
