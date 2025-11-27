# Knuth-Morris-Pratt (KMP) Algorithm

## Introduction
The Knuth-Morris-Pratt (KMP) algorithm is an efficient string matching technique used to find occurrences of a "pattern" within a "text". Unlike a naive substring search which may re-examine previously matched characters, KMP uses information gleaned from the pattern itself (via the LPS array) to skip unnecessary comparisons, resulting in faster searching.

## Usage

Import this KMP class and call the search method with the text and pattern strings.

Example:

    indices = KMP.search("ABABDABACDABABCABAB", "ABABCABAB")
    print(indices)  # Output: [10]

## Detailed Explanation
The implementation is encapsulated in the `KMP` class with two static methods:

- `compute_lps(pattern)`:
  Creates the Longest Prefix Suffix (LPS) array for the pattern. The LPS array holds the length of the longest proper prefix of the substring pattern[0..i] which is also a suffix of this substring. This information is used to avoid rechecking characters that are known to match.

- `search(text, pattern)`:
  Utilizes the LPS array to perform the search.
  - Initialize pointers for the `text` (i) and `pattern` (j).
  - Compare characters at `text[i]` and `pattern[j]`:
    - If they match, move both pointers forward.
    - If the full pattern is matched (`j == len(pattern)`), record the start index of this match and reset `j` using the LPS array to continue searching.
    - If characters don't match and `j` is not at the start, update `j` based on LPS without moving `i` to skip unnecessary comparisons.
    - Else, move `i` forward.

This approach ensures each character in the text is compared at most once, yielding a linear-time search.

## Complexity Analysis
- Time Complexity:
  - Preprocessing (LPS array creation): O(m), where m is the length of the pattern.
  - Searching: O(n), where n is the length of the text.
  - Overall: O(n + m).

- Space Complexity:
  - O(m) to store the LPS array.

This makes KMP especially efficient for large texts or repeated searches with the same pattern.