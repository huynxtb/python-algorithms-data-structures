# Boyer-Moore String Search Algorithm

## 1. Introduction
The Boyer-Moore algorithm is a highly efficient string searching algorithm used to find all occurrences of a pattern string within a larger text string. It is especially useful when searching large texts because it preprocesses the pattern to skip sections of the text, often resulting in sub-linear time complexity in practice. The algorithm achieves this performance by utilizing two heuristics: the bad character rule and the good suffix rule. These heuristics allow it to jump ahead rather than checking every character in the text.

Use Boyer-Moore when performance is critical in string matching problems, such as text editors, search engines, and DNA sequence analysis.

## 2. Usage
pattern = "example"
text = "here is an example of the example string for example purposes"

bm = BoyerMoore(pattern)
occurrences = bm.search(text)  # Returns a list of indices where pattern starts

print(occurrences)  # Expected output: [11, 23, 42]

## 3. Detailed Explanation
The implementation contains a class `BoyerMoore` which takes a pattern and preprocesses it for efficient searching:

- **Bad Character Rule Preprocessing:**
  - Creates a table of last occurrence indices of each ASCII character in the pattern.
  - When a mismatch occurs, this table tells how far we can shift the pattern based on the mismatched character's last position in the pattern.

- **Good Suffix Rule Preprocessing:**
  - Calculates shifts based on suffixes of the pattern that match substrings following the mismatch.
  - Ensures the pattern aligns with the next possible matching substring.

The actual `search` method takes a text and uses the preprocessed tables to attempt matches. When a mismatch occurs, it uses the larger of the two shifts prescribed by the heuristics (bad character or good suffix) to move forward in the text, skipping unnecessary comparisons.

## 4. Complexity Analysis
- **Time Complexity:**
  - Preprocessing: O(m + |alphabet|) where m is the length of the pattern.
  - Searching: O(n) on average, where n is the length of the text. Worst-case complexity can be O(mn) but is rare due to heuristic skips.

- **Space Complexity:**
  - O(m + |alphabet|) for storing preprocessing tables.

This implementation uses an ASCII fixed alphabet size of 256 for simplicity.