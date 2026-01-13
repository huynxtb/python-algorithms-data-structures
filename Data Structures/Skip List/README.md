# Skip List

## Introduction
A Skip List is a probabilistic, layered data structure that enables fast search, insertion, and deletion operations within an ordered sequence of elements. It provides an efficient alternative to balanced trees like AVL or Red-Black trees by using multiple levels of linked lists to skip over large parts of the list during traversal. Each element is part of one or more levels, with higher levels having fewer elements, allowing average-case logarithmic time complexity for operations.

Skip Lists are useful when you want balanced tree-like performance but prefer a simpler, randomized data structure.

---

## Usage

Initialize a skip list, insert elements, search, and delete:

skiplist = SkipList()
skiplist.insert(10)
skiplist.insert(20)
skiplist.insert(15)

print(skiplist.search(15))  # True
print(skiplist.search(99))  # False

skiplist.delete(20)
print(skiplist.search(20))  # False

---

## Detailed Explanation

The implementation consists of two main components:

- **SkipListNode**: Represents a node which holds a value and an array of forward pointers (one for each level it spans).
- **SkipList**: Encapsulates the skip list logic, including insertion, deletion, and search.

### Core Concepts

1. **Levels and Probability:**
   - Each node is assigned a level at insertion based on a random probabilistic function.
   - Higher level nodes appear less frequently.
   - `MAX_LEVEL` controls the maximum number of levels.
   - `P` determines the probability of promoting a node to a higher level.

2. **Header Node:**
   - A special node storing forward pointers for all levels to start traversal.

3. **Insertion:**
   - Find the update points at every level where the new node should be inserted.
   - Randomly generate a level for the new node.
   - Insert the node by adjusting pointers.
   - Update list's level if necessary.

4. **Deletion:**
   - Find update points similar to insertion.
   - Bypass the node if it exists.
   - Adjust the skip list's level down if needed.

5. **Search:**
   - Begin at highest level and traverse forward while next node's value is less than target.
   - Move down levels until found or absent.

This design supports average O(log n) complexity for these operations.

---

## Complexity Analysis

| Operation  | Average Time Complexity | Worst Time Complexity |
|------------|-------------------------|----------------------|
| Search     | O(log n)                | O(n)                 |
| Insert     | O(log n)                | O(n)                 |
| Delete     | O(log n)                | O(n)                 |

- **Average case:** Balanced by probabilistic levels.
- **Worst case:** Degenerates to linked list.

**Space Complexity:** O(n) due to multiple forward pointers.

---

Skip List offers a simpler randomized data structure that is often easier to implement than balanced trees with comparable performance for dynamic sorted data management.