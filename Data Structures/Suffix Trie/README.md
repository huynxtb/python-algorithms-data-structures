# Suffix Trie

## Introduction

A *Suffix Trie* is a specialized data structure that stores all suffixes of a given string in a compressed prefix trie (also known as a prefix tree). It allows efficient searching of whether a substring exists within the original string. This can be highly useful in various applications such as text search, pattern matching, bioinformatics (e.g., DNA sequence analysis), and string processing algorithms.

Unlike a straightforward trie built from all suffixes, the suffix trie can efficiently represent the suffixes without explicitly storing repeated substrings multiple times.

## Usage

To use the Suffix Trie class, instantiate it with a text string, and then invoke the `contains` method to query if any substring exists within that string.

Example usage:

trie = SuffixTrie("banana")

print(trie.contains("ana"))   # True
print(trie.contains("nana"))  # True
print(trie.contains("ban"))   # True
print(trie.contains("apple")) # False

## Detailed Explanation

- **Construction**: When the `SuffixTrie` object is instantiated with a text string, it constructs the trie by inserting every suffix of the string. Each suffix is inserted character-by-character into the trie.

- **Trie structure**: The trie is composed of nodes that map characters to their child nodes, forming branches for each suffix path.

- **Searching**: To check whether a pattern exists within the original string, the trie is traversed down using each character of the pattern. If at any point the character path doesn't exist, the pattern is not present. If the traversal completes successfully, the substring exists.

- **Memory efficiency**: While this implementation does not compress edges as a suffix tree would, it still avoids duplicated storage of suffixes by reusing common prefixes.

This design is clean, intuitive, and provides efficient substring lookup.

## Complexity Analysis

Let n be the length of the input text and m be the length of the query pattern.

- **Construction Time Complexity:** O(n^2) in the worst case, since all suffixes (n suffixes) are inserted, and each suffix can take up to O(n) operations.
- **Construction Space Complexity:** O(n^2) in the worst case due to storing all suffixes explicitly.
- **Search Time Complexity:** O(m) since each character of the pattern traverses down one level in the trie.

This structure is therefore suitable for moderate-sized inputs where fast query lookups are needed after preprocessing.

---

This class is a reusable and extensible foundation for suffix trie-based operations and can be extended or optimized further (e.g., suffix trees or suffix arrays) depending on use case requirements.