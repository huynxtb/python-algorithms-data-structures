# Trie (Prefix Tree)

## Introduction

A Trie, also known as a Prefix Tree, is a specialized tree-based data structure used primarily for storing and retrieving strings efficiently, especially when dealing with prefixes. It is widely used in applications such as autocomplete systems, spell checkers, and prefix-based search optimizations.

The Trie allows for quick lookup of words or prefixes by branching with each character, which makes checking and inserting strings very efficient compared to traditional data structures like arrays or hash sets when dealing with a large set of strings.

## Usage

# Create a new Trie instance
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("app")

# Search for an exact word
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: True
print(trie.search("appl"))    # Output: False

# Check if any word starts with a given prefix
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("apl"))  # Output: False

## Detailed Explanation

- The `Trie` class uses a nested `TrieNode` class for nodes.
- Each `TrieNode` has a dictionary named `children` mapping characters to subsequent `TrieNode` objects.
- Each node also has a boolean `is_end_of_word` to indicate if the node completes a valid word.

### Insert
- Starting from the root node, each character of the word is processed.
- If the character is not already a child of the current node, a new child node is created.
- Move to the child node corresponding to the character.
- Once all characters are processed, mark the last node's `is_end_of_word` True.

### Search
- Traverse the Trie nodes following the word's characters.
- If at any point a character is missing in the children dictionary, return False.
- After processing all characters, return True if `is_end_of_word` is True for the last node, indicating the exact word exists.

### Starts with
- Same traversal as search but return True as long as all prefix characters are found in sequence.

## Complexity Analysis

- **Insert:**
  - Time Complexity: O(m) where m is the length of the word being inserted.
  - Space Complexity: O(m) in the worst case for new nodes.

- **Search:**
  - Time Complexity: O(m) where m is the length of the word.
  - Space Complexity: O(1) as no extra space apart from traversal variables is used.

- **Starts with:**
  - Time Complexity: O(m), with m being the prefix length.
  - Space Complexity: O(1).