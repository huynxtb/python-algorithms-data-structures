# Binary Search Tree (BST)

## 1. Introduction
A Binary Search Tree (BST) is a node-based binary tree data structure. For any given node, the values of all nodes in its left subtree are less than the node's value, and the values of all nodes in its right subtree are greater than the node's value. BSTs are used for efficient searching, insertion, and deletion operations, and they serve as the foundation for more complex structures like AVL trees and Red-Black trees.

## 2. Usage

# Initialize the tree
bst = BinarySearchTree()

# Insert values
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

# Search for a value
node = bst.search(30)
if node:
    print(f"Found node: {node.val}")

# Delete a value
bst.delete(30)

# Retrieve traversals
print("Inorder:", bst.inorder())    # Output: [20, 40, 50, 70]
print("Preorder:", bst.preorder())  # Output: [50, 20, 40, 70]
print("Postorder:", bst.postorder())# Output: [40, 20, 70, 50]


## 3. Detailed Explanation
- **Insertion**: Recursively traverses down the tree. Compares the target value with the current node's value to decide whether to go left or right, placing the new node at the first empty spot (`None`).
- **Search**: Recursively compares the target value with the current node's value, branching left if smaller and right if larger, until the value is found or a leaf is reached.
- **Deletion**: Handles three cases:
  1. *Leaf Node*: The node is removed directly.
  2. *One Child*: The node is replaced by its single child.
  3. *Two Children*: The node's value is replaced by its inorder successor (the minimum value in its right subtree), and the inorder successor node is then deleted.
- **Traversals**:
  - *Inorder*: Left subtree, Root, Right subtree (yields sorted order).
  - *Preorder*: Root, Left subtree, Right subtree.
  - *Postorder*: Left subtree, Right subtree, Root.

## 4. Complexity Analysis
- **Time Complexity**:
  - **Search**: $O(h)$ average $O(\log n)$, worst-case $O(n)$ for skewed trees.
  - **Insertion**: $O(h)$ average $O(\log n)$, worst-case $O(n)$.
  - **Deletion**: $O(h)$ average $O(\log n)$, worst-case $O(n)$.
  - **Traversals**: $O(n)$ as every node is visited exactly once.
- **Space Complexity**:
  - **Operations**: $O(h)$ auxiliary space for the recursion stack, where $h$ is the height of the tree.
  - **Traversals**: $O(n)$ to store the returned list of node values.