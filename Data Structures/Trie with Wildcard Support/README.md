# Trie with Wildcard Support

## 1. Introduction

The Trie with Wildcard Support is an advanced data structure based on the classical Trie (Prefix Tree). It is designed for efficient storage and retrieval of words, with enhanced capability to support search patterns containing a wildcard character '?'. The '?' character matches exactly one arbitrary lowercase English letter ('a' to 'z').

This makes the structure particularly useful in applications like autocomplete, spell-checkers, pattern searching, and anywhere flexible pattern matching is needed.

## 2. Usage

# Create a Trie instance
trie = Trie()

# Insert words
trie.insert("cat")
trie.insert("cot")
trie.insert("cut")
trie.insert("dog")

# Search with exact match
print(trie.search("cat"))  # Output: True
print(trie.search("bat"))  # Output: False

# Search with wildcard '?'
print(trie.search("c?t"))  # Output: True (matches "cat", "cot", "cut")
print(trie.search("d?g"))  # Output: True (matches "dog")
print(trie.search("??g"))  # Output: True (matches "dog")
print(trie.search("???"))  # Output: True (matches words with length 3)
print(trie.search("????")) # Output: False (no 4-letter words inserted)

## 3. Detailed Explanation

- **Insertion:**
  - Each word is inserted by traversing the Trie from the root.
  - For every character in the word, if the character node doesn't exist, it is created.
  - After the last character, the node is marked as the end of a word.

- **Search:**
  - To support the wildcard '?', a depth-first search (DFS) is performed.
  - If the current character in the pattern is a normal character, search moves down the Trie following that character’s child node.
  - If the character is '?', the search branches out recursively to all possible child nodes, because '?' can represent exactly one character.
  - The pattern matches a word in the Trie only if the traversal reaches the end of the pattern exactly at a node marked as an end of a word.

This recursion ensures flexible and efficient pattern matching.

## 4. Complexity Analysis

- **Time Complexity:**
  - Insertion: O(m) where m is the length of the word
  - Search:
    - Without wildcards: O(m)
    - With wildcards: O(k^m) in the worst case, where k is the branching factor (up to 26), due to the recursive exploration for '?' characters. However, typical usage and pruning reduce this drastically.

- **Space Complexity:**
  - O(N * m) where N is the number of words inserted and m is the average length of the words, since each node represents part of a word prefix.

The Trie structure is space-efficient for large sets of overlapping word prefixes and supports very fast query operations, especially useful when implemented to accommodate wildcards as above.