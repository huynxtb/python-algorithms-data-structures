# Dancing Links (DLX) Algorithm

## 1. Introduction

Dancing Links (DLX) is an efficient algorithm for solving the exact cover problem, invented by Donald Knuth. The exact cover problem involves finding a subset of rows from a binary matrix such that each column contains exactly one '1'. DLX is especially useful for solving constraint satisfaction problems like Sudoku solving, polyomino tiling, and set cover problems.

DLX uses specialized doubly linked lists to efficiently cover and uncover columns and rows during backtracking, hence its name "Dancing Links". This data structure allows fast undo operations, making the search for solutions very efficient.

## 2. Usage

# Suppose you have a binary matrix representing the exact cover problem:
matrix = [
    [0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    # ... more rows
]

# Create a DancingLinks instance
solver = DancingLinks(matrix)

# Find one solution (a list of row indices)
solution = solver.solve(find_all=False)

# Find all solutions
all_solutions = solver.solve(find_all=True)

# Each solution is a list of row indices that form an exact cover.

## 3. Detailed Explanation

- **Data Structures:**
  - **DLXNode:** Represents a node in a doubly-linked list with pointers left, right, up, down and a reference to its column.
  - **DLXColumn:** Inherits from DLXNode, adds size (count of nodes in the column) and a name for identification.
  - The entire binary matrix is represented as a toroidal doubly linked list, where each node corresponds to a '1' in the matrix.

- **Initialization:**
  - Creates a root column header.
  - Columns are linked horizontally.
  - For each row, nodes for non-zero entries are created and linked horizontally and vertically.

- **Cover/Uncover Operations:**
  - **Cover:** Removes a column from the structure and all rows that have a node in this column.
  - **Uncover:** Restores the column and the rows.
  - These are used to efficiently reduce the search space as choices are made.

- **Search Procedure:**
  - Recursively search for an exact cover.
  - Choose a column with minimum size (heuristic to improve speed).
  - Cover that column and try each row in it.
  - Recursively solve on the reduced matrix.
  - Backtrack by uncovering columns and removing choices.

## 4. Complexity Analysis

- **Time Complexity:**
  - The worst-case complexity is exponential since exact cover is NP-complete.
  - The heuristic of choosing the column with the smallest size helps prune the search tree.
  - Cover and uncover operations run in O(k) where k is the number of nodes in the respective columns and rows.

- **Space Complexity:**
  - O(n + m + t) where n = number of rows, m = number of columns, and t = total number of '1's in the matrix (nodes).
  - This is required to store the linked nodes and auxiliary structure.

This implementation provides a clean, reusable interface without runtime I/O and can efficiently be integrated into various exact cover problems.