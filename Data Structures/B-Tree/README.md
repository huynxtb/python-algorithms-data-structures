# B-Tree Implementation in Python

## 1. Introduction
A **B-Tree** is a self-balancing search tree in which each node can contain more than one key and more than two children. Parameterized by a minimum degree $t \ge 2$:
- Every node other than the root must contain at least $t - 1$ keys.
- Every node can contain at most $2t - 1$ keys.
- Every internal node with $k$ keys has $k + 1$ children.
- All leaves appear at the same depth.

B-Trees are optimized for systems that read and write large blocks of memory (such as hard drives, SSDs, database management systems, and filesystems) because high branching factors reduce tree height and disk I/O operations.

## 2. Usage


from btree import BTree

# Create a B-Tree of minimum degree t=3 (order 5)
tree = BTree[int](t=3)

# Insert elements
for val in [10, 20, 5, 6, 12, 30, 7, 17]:
    tree.insert(val)

# Search for keys
found = tree.search(12)
if found is not None:
    node, idx = found
    print(f"Key found: {node.keys[idx]}")

# In-order traversal
print("Sorted keys:", tree.inorder_traversal())

# Delete elements
tree.delete(6)
tree.delete(10)
print("Keys after deletion:", tree.inorder_traversal())


## 3. Detailed Explanation

### Insertion (`insert`)
Insertion proceeds preemptively top-down:
1. If the root node is full ($2t - 1$ keys), a new root is created, and the old root is split into two halves, with the median key moving up to the new root.
2. When descending the tree, any child node that is full is split before traversing into it. This guarantees that recursive insertions have sufficient space without needing upward re-balancing.

### Deletion (`delete`)
Deletion handles all classic CLRS B-Tree structural cases to ensure minimum degree constraints are preserved ($t - 1$ keys per non-root node):
1. **Key in Leaf:** Remove key directly.
2. **Key in Internal Node:**
   - If the left child has at least $t$ keys, replace key with its in-order predecessor and recursively delete the predecessor.
   - If the right child has at least $t$ keys, replace key with its in-order successor and recursively delete the successor.
   - If both have $t - 1$ keys, merge the key and right child into the left child, then recursively delete from the merged child.
3. **Key in Subtree:** Before descending to a child with $t - 1$ keys, ensure it is enriched with an additional key via borrowing from an adjacent sibling with $\ge t$ keys or merging with a sibling.

## 4. Complexity Analysis

- **Time Complexity**:
  - **Search**: $\mathcal{O}(t \log_t n)$ or $\mathcal{O}(\log n)$
  - **Insert**: $\mathcal{O}(t \log_t n)$
  - **Delete**: $\mathcal{O}(t \log_t n)$
  - **In-Order Traversal**: $\mathcal{O}(n)$
- **Space Complexity**:
  - Storage: $\mathcal{O}(n)$ total space for storing $n$ keys.
  - Call Stack / Auxiliary: $\mathcal{O}(\log_t n)$ recursion depth.