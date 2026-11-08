# Two-Dimensional Array Rotation

## Introduction
The Two-Dimensional Array Rotation algorithm is used to rotate a given square matrix (2D array) by 90 degrees clockwise. This is particularly useful in various applications such as image processing, where images can be represented as matrices.

## Usage
Here is a simple example of how to use the `rotate` function:

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotated_matrix = rotate(matrix)
print(rotated_matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


## Detailed Explanation
The algorithm works in two main steps:
1. **Transpose the Matrix:** This involves swapping elements such that the rows become columns. For a matrix element at position (i, j), it is swapped with the element at (j, i).
2. **Reverse Each Row:** After transposing, each row of the matrix is reversed to achieve the final rotated matrix.

This approach modifies the matrix in place, which means it does not require additional space proportional to the size of the input matrix, making it efficient.

## Complexity Analysis
- **Time Complexity:** O(n^2), where n is the number of rows (or columns) in the matrix. This is because we need to traverse each element of the matrix twice (once for transposing and once for reversing).
- **Space Complexity:** O(1), as we are performing the rotation in place without using any additional data structures.