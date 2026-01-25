# Knapsack Problem using Dynamic Programming

## 1. Introduction

The 0/1 Knapsack Problem is a classic optimization problem where you are given a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity. The goal is to determine the subset of items that fits within the capacity such that the total value is maximized. This Python implementation uses Dynamic Programming (DP) to solve the problem optimally. 

This solution is useful when you want to solve the problem efficiently without enumerating all subsets, which would be exponentially complex. It's foundational in computer science, illustrating the power of DP in optimization problems.

## 2. Usage

from KnapsackDP import KnapsackDP

items = [(2, 3), (1, 2), (3, 4), (2, 2)]  # each tuple is (weight, value)
capacity = 5

knapsack = KnapsackDP(items, capacity)
max_value = knapsack.get_max_value()
selected_items = knapsack.get_selected_items()

# max_value now holds the maximum total value achievable within the weight limit.
# selected_items is the list of items chosen to achieve this maximum value.

## 3. Detailed Explanation

- **Initialization:** You provide a list of items as tuples of (weight, value) and a capacity.
- **DP Table Construction:** A 2D list `dp` of size `(number_of_items + 1) x (capacity + 1)` is built where `dp[i][w]` represents the maximum value achievable using the first `i` items with a weight limit `w`.
- **Transition:** For each item and for each capacity `w`, if the item can fit (`weight <= w`), the algorithm decides whether to include it or not by comparing the value of including it (`dp[i-1][w-weight] + value`) versus excluding it (`dp[i-1][w]`).
- **Result Extraction:** The maximum value is found at `dp[n][capacity]`. To find the selected items, backtracking is done from `dp[n][capacity]` to determine which items contributed to the final value.

## 4. Complexity Analysis

- **Time Complexity:** O(n * W), where `n` is the number of items, and `W` is the capacity. This is because each entry of the DP table is computed exactly once.
- **Space Complexity:** O(n * W) for the DP table storage.

This solution is efficient for moderate values of `n` and `W`. For very large capacities, space and time optimization techniques or approximation algorithms might be necessary.