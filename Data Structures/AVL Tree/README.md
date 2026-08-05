# AVL Tree

## 1. Introduction
An AVL Tree is a self-balancing binary search tree (BST) where the difference between heights of left and right subtrees (the balance factor) cannot be more than 1 for all nodes. It is used when lookup operations are more frequent than insertion and deletion operations, ensuring $O(\log n)$ search times.

## 2. Usage

tree = AVLTree()
tree.insert(10, "Value A")
tree.insert(20, "Value B")
tree.insert(5, "Value C")

# Search for a key
result = tree.search(20)  # Returns "Value B"

# Delete a key
tree.delete(10)


## 3. Detailed Explanation
The implementation consists of two classes:
- `AVLNode`: Represents a node containing a key, value, left child, right child, and height.
- `AVLTree`: Manages the tree structure and balancing logic.

### Balancing Operations
When insertions or deletions cause a node's balance factor to exceed 1 or fall below -1, rotations are performed:
- **Left-Left (LL) Case**: Solved by a single right rotation.
- **Right-Right (RR) Case**: Solved by a single left rotation.
- **Left-Right (LR) Case**: Solved by a left rotation on the left child, followed by a right rotation on the node.
- **Right-Left (RL) Case**: Solved by a right rotation on the right child, followed by a left rotation on the node.

## 4. Complexity Analysis
- **Time Complexity**:
  - Search: $O(\log n)$
  - Insertion: $O(\log n)$
  - Deletion: $O(\log n)$
- **Space Complexity**: $O(n)$ to store $n$ elements in the tree.