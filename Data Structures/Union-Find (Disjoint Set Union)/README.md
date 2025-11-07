# Union-Find (Disjoint Set Union)

## 1. Introduction

Union-Find, also known as Disjoint Set Union (DSU), is a data structure that keeps track of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides efficient methods for:
- Finding which subset a particular element belongs to.
- Merging two subsets into a single subset.

This data structure is essential in solving dynamic connectivity problems, such as determining whether two nodes in a network are connected, or for algorithms like Kruskal's Minimum Spanning Tree.

## 2. Usage

uf = UnionFind(10)  # Create 10 elements, each in its own set
uf.union(1, 2)      # Merge sets containing elements 1 and 2
uf.union(3, 4)      # Merge sets containing elements 3 and 4
print(uf.connected(1, 2))  # Returns True
print(uf.connected(1, 3))  # Returns False
uf.union(2, 3)      # Merge sets containing elements 2 and 3
print(uf.connected(1, 4))  # Returns True

## 3. Detailed Explanation

- **Initialization:**
  - Each element is initially in its own set where the element is the root of itself.
  - An array `parent` is maintained where `parent[i]` refers to the parent of element `i`. Initially, `parent[i] = i`.
  - An auxiliary `size` array tracks the size of the tree rooted at each element for efficient union.

- **Find Operation with Path Compression:**
  - The `find(x)` method returns the root representative of the set containing `x`.
  - To optimize queries, path compression is applied: during the find, the parent pointer of each visited node is updated directly to the root, flattening the structure and speeding up future operations.

- **Union Operation by Size:**
  - The `union(x, y)` method merges the sets containing `x` and `y`.
  - The roots of both sets are found.
  - The smaller set (by size) is merged under the larger set to keep the tree shallow.

- **Connected Check:**
  - The `connected(x, y)` method checks if `x` and `y` are in the same set by comparing their roots.

## 4. Complexity Analysis

- **Time Complexity:**
  - Both `find` and `union` operations run in approximately O(\alpha(n)), where \alpha is the inverse Ackermann function, which is very slow growing and for all practical values can be considered almost constant.
  - `connected` operation also runs in O(\alpha(n)) due to its reliance on `find`.

- **Space Complexity:**
  - O(n) for storing the `parent` and `size` arrays.

This efficient data structure lends itself well to problems involving dynamic connectivity, grouping, and partitioning efficiently under union and find operations.