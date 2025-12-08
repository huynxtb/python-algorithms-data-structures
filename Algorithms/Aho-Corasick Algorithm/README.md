# Aho-Corasick Algorithm

## Introduction

The Aho-Corasick algorithm is a fundamental string-searching algorithm that efficiently finds all occurrences of multiple patterns (keywords) within a given text simultaneously. It constructs a finite automaton for the given set of keywords allowing you to perform multiple pattern matching in linear time relative to the text length plus the sum of the keyword lengths. This makes it especially useful in scenarios like spam filtering, dictionary-based searching, intrusion detection, and autocomplete systems.

## Usage

# Creating an instance of AhoCorasick with a list of keywords
keywords = ["he", "she", "his", "hers"]
ac = AhoCorasick(keywords)

# Build the failure links after insertion (if keywords were inserted manually, call build_failures())
# ac.build_failures()

# Search text for the keywords
text = "ushers"
matches = ac.search(text)
print(matches)  # Output: {'she': [2], 'he': [3], 'hers': [2]}

## Detailed Explanation

The implementation consists of a main class `AhoCorasick` with a nested `Node` class representing each state in the trie:

- **Insertion**: Insert each keyword into a trie, where each node corresponds to a character. The `output` list in a node stores patterns that end at that node.

- **Failure Links Building**: Perform a breadth-first search (BFS) over the trie nodes to populate `fail` pointers. Failure links provide fallback transitions when a mismatch occurs, allowing the automaton to continue matching from the longest possible suffix.
  The root node's children have failure links pointing back to the root.

- **Search**: For each character in the input text, follow the trie edges if possible; otherwise, use failure links to fallback. When landing on a node, all patterns in its `output` list correspond to matches ending at the current position.

The `search` method returns a dictionary mapping each found keyword to a list of all starting indices where it occurs in the text.

## Complexity Analysis

- **Time Complexity**:
  - Building the trie from `k` keywords with total length `L`: O(L)
  - Building failure links: O(L) because every node is visited once in BFS.
  - Searching text of length `n`: O(n + z), where `z` is the total number of matches found.

- **Space Complexity**:
  - The trie nodes and edges require O(L) space.
  - Additional space for the failure links and output lists also aggregate to O(L).

This results in an efficient algorithm suitable for fast multi-pattern matching tasks in large texts.