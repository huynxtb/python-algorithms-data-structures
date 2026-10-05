# Hungarian (Kuhn-Munkres) Algorithm

## 1. Introduction
The Hungarian Algorithm (also known as the Kuhn-Munkres Algorithm) is a combinatorial optimization method that solves the assignment problem in polynomial time. Given an $N \times M$ cost matrix representing bipartite matching weights (e.g., assigning $N$ workers to $M$ tasks), the algorithm determines a one-to-one assignment that minimizes (or maximizes) the total cost.

Common applications include:
- Resource and task allocation.
- Tracking and object association in computer vision.
- Facility location problems.
- Optimal network routing and bipartite maximum weight matching.

## 2. Usage


from hungarian_algorithm import hungarian_algorithm

# Cost matrix: 3 workers (rows) and 3 jobs (columns)
cost_matrix = [
    [80, 40, 50],
    [40, 70, 20],
    [30, 10, 20]
]

# Minimize total cost
assignment, total_cost = hungarian_algorithm(cost_matrix, maximize=False)
print("Optimal pairs:", assignment)  # [(0, 1), (1, 2), (2, 0)]
print("Total cost:", total_cost)     # 40 + 20 + 30 = 90

# Maximize total profit
profit_matrix = [
    [7, 9, 8, 9],
    [2, 8, 5, 7],
    [1, 6, 6, 9]
]
assignment, total_profit = hungarian_algorithm(profit_matrix, maximize=True)
print("Optimal pairs:", assignment)
print("Total profit:", total_profit)


## 3. Detailed Explanation
The implementation is based on the modern dual-variable formulation maintaining potentials $u_i$ (for rows) and $v_j$ (for columns) such that reduced costs $c'_{i, j} = c_{i, j} - u_i - v_j \ge 0$.

Key steps include:
1. **Rectangular Padding & Transformation**: Rectangular $N \times M$ inputs are padded into square matrices of size $\max(N, M) \times \max(N, M)$. Maximization is transformed to minimization by negating matrix entries.
2. **Augmenting Path Search**: The algorithm iterates row by row ($O(V)$ iterations). In each iteration, it performs Dijkstra-like slack relaxation across columns using a `minv` array.
3. **Potential Reduction**: Dual variables $u$ and $v$ are updated using the minimal slack $\delta$, maintaining complementary slackness.
4. **Augmentation**: When an unassigned column is reached, the alternating path is traversed backward using the `way` array, augmenting the matching.
5. **Filtering**: Dummy rows and columns added during padding are pruned, returning only genuine index pairs.

## 4. Complexity Analysis
- **Time Complexity**: $\mathcal{O}(V^3)$ where $V = \max(N, M)$. Finding each augmenting path inspects $\mathcal{O}(V^2)$ edges/potentials, and there are $V$ augmenting path stages.
- **Space Complexity**: $\mathcal{O}(V^2)$ auxiliary space to store the padded square matrix and $\mathcal{O}(V)$ space for potential arrays ($u, v$), slack arrays (`minv`), and matching references (`p`, `way`).