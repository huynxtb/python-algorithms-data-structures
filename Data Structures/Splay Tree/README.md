# Splay Tree

## 1. Introduction
A **Splay Tree** is a self-adjusting binary search tree (BST) invented by Daniel Sleator and Robert Tarjan in 1985. The key characteristic of a splay tree is the **splay operation**: every time an element is accessed (inserted, searched, or deleted), it is moved to the root of the tree through a specific sequence of tree rotations.

Splay trees do not require explicit balance factor or color bookkeeping (unlike AVL or Red-Black trees), yet they achieve **amortized $O(\log n)$** time complexity for all basic operations. They are ideal for applications exhibiting non-uniform access patterns, such as:
- Caches and working-set environments where recently accessed data is likely to be accessed again (temporal locality).
- Network routing tables and data compression algorithms (e.g., dynamic Huffman coding).

## 2. Usage


# Initialize a splay tree
tree = SplayTree()

# Insert elements
for val in [50, 20, 70, 10, 30, 60, 80]:
    tree.insert(val)

# Membership / Search
print(30 in tree)       # True (splays 30 to root)
print(tree.search(100)) # False (splays last accessed node to root)

# Minimum and Maximum
print(tree.minimum())   # 10
print(tree.maximum())   # 80

# In-order traversal
print(tree.inorder())   # [10, 20, 30, 50, 60, 70, 80]

# Deletion
tree.delete(30)
print(len(tree))        # 6


## 3. Detailed Explanation

The fundamental operation is **Splaying**, which brings a target node $x$ to the root using three types of step transitions based on the relative position of $x$, its parent $p$, and its grandparent $g$:

1. **Zig**: When $p$ is the root of the tree ($g$ is `None`), a single rotation around $p$ is performed (left rotation if $x$ is the right child, right rotation if $x$ is the left child).
2. **Zig-Zig**: When $x$ and $p$ are both left children or both right children. The tree is rotated first around $g$, and then around $p$. This order is critical for halving the depth of trees.
3. **Zig-Zag**: When $x$ is a right child and $p$ is a left child (or vice versa). A standard double rotation is performed: rotate around $p$, then around $g$.

### Key Operations:
- **`insert(key)`**: Inserts the key as in a standard BST and splays the new node to the root. If the key already exists, the existing node is splayed.
- **`search(key)`**: Traverses down to find the key. If found, the node is splayed; if not, the last visited node is splayed to the root.
- **`delete(key)`**: Splays the key to the root (raising `KeyError` if absent). Then removes the root and joins the left and right subtrees by splaying the maximum node of the left subtree to its root, attaching the right subtree as its right child.

## 4. Complexity Analysis

| Operation | Amortized Time | Worst-Case Time | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **Insert** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **Delete** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **Min / Max** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **In-Order** | $O(n)$ | $O(n)$ | $O(n)$ recursion / result |

- **Space Complexity**: $O(n)$ total space where each node stores a key and three pointers (`left`, `right`, `parent`).