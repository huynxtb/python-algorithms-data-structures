# Red-Black Tree

## 1. Introduction

A Red-Black Tree is a type of self-balancing binary search tree designed to maintain a balanced height while allowing efficient insertion, deletion, and searching operations. It ensures approximately balanced tree height by applying color properties to its nodes, which guarantees that the longest path from the root to a leaf is no more than twice the length of the shortest path.

The main properties that define a Red-Black Tree are:
- Each node is either red or black.
- The root is always black.
- Red nodes cannot have red children (no two reds in a row).
- Every path from a node to its descendant NIL (null) nodes has the same number of black nodes.

These rules guarantee logarithmic height, ensuring operations run in O(log n) time.

### When to use?
Use Red-Black Trees when you need a balanced binary search tree to support dynamic sets with frequent insertions and deletions combined with quick search operations, such as in associative arrays, priority queues, and other ordered data structures.


## 2. Usage

# Example usage of RedBlackTree
rb_tree = RedBlackTree()

# Insert values
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)

# Search for an element
found = rb_tree.search(20)  # Returns 20 if found, None otherwise

# Inorder traversal to get sorted elements
sorted_elements = rb_tree.inorder()

# Delete a value
rb_tree.delete(20)

# Traversal after deletion
sorted_after_delete = rb_tree.inorder()


## 3. Detailed Explanation

The implementation consists of two main classes: `RedBlackNode` and `RedBlackTree`.

- **RedBlackNode**:
  - Represents a node containing a key, color (red or black), and pointers to its parent, left, and right child nodes.
  - Uses a sentinel NIL node to represent leaves, simplifying boundary conditions.

- **RedBlackTree**:
  - Maintains the root of the tree and the NIL sentinel node shared by all leaf references.
  - Implements binary search tree insertion and deletion.
  - Maintains Red-Black properties through rotations and color adjustments after insertions and deletions.

### Core Operations

- **Insertion:**
  - Inserts the node as in a regular binary search tree.
  - Colors the new node red.
  - Performs fix-up operations (`insert_fixup`) to maintain Red-Black properties using rotations and recoloring.

- **Deletion:**
  - Finds the node.
  - Uses standard BST deletion rules.
  - If a black node is removed, performs `delete_fixup` to maintain properties through rotations and recoloring.

- **Rotations:**
  - Left and right rotations re-balance the tree locally, preserving the binary search tree property.

- **Search:**
  - Traverses the tree like a standard BST to find a given key.

- **Traversal:**
  - In-order traversal lists elements in ascending order.


## 4. Complexity Analysis

- **Time Complexity:**
  - Search: O(log n) average and worst case.
  - Insertion: O(log n) due to traversal and fix-up operations.
  - Deletion: O(log n) due to traversal and fix-up operations.
  - Traversal: O(n), where n is the number of elements (for inorder traversal).

- **Space Complexity:**
  - O(n) for storing all nodes.
  - Additional space for recursive call stack during traversal is O(h) (h is tree height) but generally O(log n).

This implementation uses a sentinel NIL node to simplify boundary conditions and avoid null checks, improving clarity and correctness.

---

This implementation offers a complete and clean Red-Black Tree structure suitable for use as a balanced dictionary or set in Python environments where native balanced trees are not available.