# Treap (Cartesian Tree / Randomized Binary Search Tree)

## 1. Introduction
A **Treap** (a portmanteau of *Tree* and *Heap*) is a randomized binary search tree data structure. Each node in a treap maintains two values:
1. A **Key**, satisfying standard **Binary Search Tree (BST)** ordering (in-order traversal yields keys in ascending order).
2. A **Priority**, randomly assigned upon insertion, satisfying the **Max-Heap** property (the parent's priority is strictly greater than or equal to its children's priorities).

Treaps provide simple and elegant self-balancing behavior without requiring the complex rebalancing invariants found in AVL or Red-Black trees. By randomly selecting priorities, the tree structure behaves like a BST built from a random insertion order, yielding expected logarithmic performance for all core operations.

## 2. Usage


from treap import Treap

# Initialize an empty Treap
treap = Treap[int]()

# Insert elements
for val in [50, 30, 70, 20, 40, 60, 80]:
    treap.insert(val)

print(f"Total nodes: {len(treap)}")  # Output: 7
print(f"Contains 30: {30 in treap}")  # Output: True
print(f"Contains 99: {99 in treap}")  # Output: False

# In-order traversal produces sorted keys
print(f"Sorted keys: {treap.inorder()}")
# Output: [20, 30, 40, 50, 60, 70, 80]

# Order-statistic search (1-indexed)
print(f"1st smallest: {treap.find_kth_smallest(1)}")  # Output: 20
print(f"4th smallest: {treap.find_kth_smallest(4)}")  # Output: 50
print(f"7th smallest: {treap.find_kth_smallest(7)}")  # Output: 80

# Delete an element
treap.delete(30)
print(f"After deleting 30: {treap.inorder()}")
# Output: [20, 40, 50, 60, 70, 80]


## 3. Detailed Explanation

### Core Properties
- **BST Invariant**: For every node $u$ with left child $L$ and right child $R$, $\text{key}(L) < \text{key}(u) < \text{key}(R)$.
- **Heap Invariant**: For every node $u$ with children $v$, $\text{priority}(u) \ge \text{priority}(v)$.

### Rotations
When an insertion or deletion temporarily violates the heap invariant, standard tree rotations (`_rotate_left` and `_rotate_right`) restore balance locally without disrupting the BST ordering.

### Subtree Sizes & Order Statistics
Each node maintains a `size` field representing the count of nodes in its subtree (`1 + size(left) + size(right)`). This allows rank queries and finding the $k$-th smallest element in $O(\log n)$ expected time by comparing $k$ against `size(left) + 1`.

## 4. Complexity Analysis

| Operation | Expected Time | Worst-Case Time | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Search / Contains** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **Insert** | $O(\log n)$ | $O(n)$ | $O(\log n)$ recursion stack |
| **Delete** | $O(\log n)$ | $O(n)$ | $O(\log n)$ recursion stack |
| **Find $k$-th Smallest** | $O(\log n)$ | $O(n)$ | $O(1)$ auxiliary |
| **In-Order Traversal** | $O(n)$ | $O(n)$ | $O(n)$ |
| **Total Space** | $O(n)$ | $O(n)$ | $O(n)$ |