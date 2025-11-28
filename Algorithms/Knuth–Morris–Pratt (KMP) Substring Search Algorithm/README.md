# Knuth–Morris–Pratt (KMP) Substring Search Algorithm

## Introduction
The Knuth–Morris–Pratt (KMP) algorithm is a classical string searching or substring search algorithm designed to efficiently find occurrences of a "pattern" string within a larger "text" string. It improves on the naive substring search by utilizing preprocessing of the pattern to avoid redundant comparisons, resulting in linear time complexity relative to the lengths of the text and pattern.

## Usage
Following is a simple usage example of the implemented KMP algorithm in Python:

# Assume the code is imported or defined above
text = "abxabcabcaby"
pattern = "abcaby"
indices = kmp_search(text, pattern)
print("Pattern found at indices:", indices)
# Output: Pattern found at indices: [6]

Here, the `kmp_search` function returns a list of starting indices where the pattern occurs in the text.

## Detailed Explanation
The implementation consists of two main parts:

1. **Building the LPS (Longest Prefix Suffix) Array:**
   - The LPS array stores the lengths of the longest proper prefix which is also a suffix for every prefix of the pattern.
   - This array helps in knowing where to resume the pattern check after a mismatch.
   - For each index `i` in the pattern, `lps[i]` gives the length of the longest prefix that is also a suffix ending at `i` (but excluding the whole substring itself).

2. **KMP Search Function:**
   - Uses two pointers: one for the text and one for the pattern.
   - On character matches, both pointers advance.
   - On mismatch, it uses the LPS array to shift the pattern pointer efficiently instead of restarting from zero.
   - This skipping reduces the total number of comparisons significantly.
   - When the pattern pointer reaches the end, it records a successful match starting index.

## Complexity Analysis
- **Time Complexity:** O(n + m)
  - `n` is the length of the text and `m` is the length of the pattern.
  - The preprocessing (LPS construction) takes O(m).
  - The searching phase takes O(n) due to the efficient skipping provided by the LPS array.

- **Space Complexity:** O(m) for the LPS array.

The KMP algorithm is very efficient for scenarios needing multiple substring searches or searching in large texts, especially when patterns themselves have repetitive substructures.