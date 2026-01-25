class KnapsackDP:
    def __init__(self, items, capacity):
        """
        Initialize the KnapsackDP solver.

        :param items: List of tuples (weight, value) where weight and value are integers.
        :param capacity: Integer representing maximum weight capacity of the knapsack.
        """
        self.items = items
        self.capacity = capacity
        self.n = len(items)
        self._dp = None
        self._computed = False

    def _build_dp_table(self):
        """
        Build the DP table to find the maximum value.
        """
        n, W = self.n, self.capacity
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            weight, value = self.items[i-1]
            for w in range(W + 1):
                if weight <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
                else:
                    dp[i][w] = dp[i-1][w]

        self._dp = dp
        self._computed = True

    def get_max_value(self):
        """
        Returns the maximum value achievable within the capacity constraint.

        :return: Integer maximum value.
        """
        if not self._computed:
            self._build_dp_table()
        return self._dp[self.n][self.capacity]

    def get_selected_items(self):
        """
        Returns a list of items (weight, value) representing the chosen subset that produces the maximum value.

        :return: List of tuples (weight, value).
        """
        if not self._computed:
            self._build_dp_table()

        selected = []
        w = self.capacity

        for i in range(self.n, 0, -1):
            if self._dp[i][w] != self._dp[i-1][w]:
                item = self.items[i-1]
                selected.append(item)
                w -= item[0]

        selected.reverse()  # optional to maintain original order
        return selected
