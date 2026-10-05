from typing import List, Tuple, Union
import math


def hungarian_algorithm(
    cost_matrix: List[List[Union[float, int]]],
    maximize: bool = False
) -> Tuple[List[Tuple[int, int]], Union[float, int]]:
    """Solves the linear sum assignment problem using the Hungarian (Kuhn-Munkres) Algorithm.

    Finds the optimal assignment of rows (workers) to columns (tasks) such that
    the total cost is minimized (or maximized if maximize=True).
    Supports rectangular matrices (N != M) and both integer and floating-point costs.

    Args:
        cost_matrix: A 2D list of numeric values where cost_matrix[i][j] represents
            the cost of assigning row i to column j.
        maximize: If True, solves for the maximum weight matching. Default is False.

    Returns:
        A tuple (assignments, total_cost) where:
            - assignments: A list of (row_idx, col_idx) pairs representing the optimal assignment.
              If rows <= cols, every row is matched. If rows > cols, min(rows, cols) pairs are returned.
            - total_cost: The sum of the original costs of the assigned pairs.

    Time Complexity:
        O(max(N, M)^3) where N and M are the matrix dimensions.
    Space Complexity:
        O(max(N, M)^2) for internal padding and potential vectors.
    """
    if not cost_matrix or not cost_matrix[0]:
        return [], 0

    original_rows = len(cost_matrix)
    original_cols = len(cost_matrix[0])

    for row in cost_matrix:
        if len(row) != original_cols:
            raise ValueError("All rows in cost_matrix must have the same length.")

    n = max(original_rows, original_cols)

    # Determine padding cost
    # If maximizing, we negate values for standard minimization.
    # Dummy entries must not interfere with optimal assignments.
    if maximize:
        max_val = max(max(row) for row in cost_matrix)
        min_val = min(min(row) for row in cost_matrix)
        pad_val = min_val - 1.0
    else:
        max_val = max(max(row) for row in cost_matrix)
        pad_val = max_val + 1.0

    # Build square matrix
    matrix: List[List[float]] = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < original_rows and j < original_cols:
                val = float(cost_matrix[i][j])
                matrix[i][j] = -val if maximize else val
            else:
                matrix[i][j] = -pad_val if maximize else pad_val

    # 1-based indexing for Kuhn-Munkres implementation with dual variables
    u = [0.0] * (n + 1)
    v = [0.0] * (n + 1)
    p = [0] * (n + 1)  # p[j] = row matched to column j
    way = [0] * (n + 1)  # way[j] = column through which potential update occurred

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [math.inf] * (n + 1)
        used = [False] * (n + 1)

        while True:
            used[j0] = True
            i0 = p[j0]
            delta = math.inf
            j1 = 0

            for j in range(1, n + 1):
                if not used[j]:
                    cur = matrix[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            for j in range(0, n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1
            if p[j0] == 0:
                break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    assignment_map = {}
    for j in range(1, n + 1):
        if p[j] > 0:
            assignment_map[p[j] - 1] = j - 1

    assignments: List[Tuple[int, int]] = []
    total_cost: Union[float, int] = 0
    is_all_int = all(
        isinstance(cost_matrix[r][c], int)
        for r in range(original_rows)
        for c in range(original_cols)
    )

    for i in range(original_rows):
        j = assignment_map.get(i)
        if j is not None and j < original_cols:
            assignments.append((i, j))
            total_cost += cost_matrix[i][j]

    if is_all_int:
        total_cost = int(round(total_cost))

    return assignments, total_cost
