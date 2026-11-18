class MedianOfMedians:
    def select(self, arr, k):
        if len(arr) == 1:
            return arr[0]
        # Divide arr into sublists of 5
        sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
        medians = [self.median(sublist) for sublist in sublists]
        # Find the median of the medians
        pivot = self.select(medians, len(medians) // 2)
        # Partitioning step
        low = [x for x in arr if x < pivot]
        high = [x for x in arr if x > pivot]
        k_index = len(low)
        if k < k_index:
            return self.select(low, k)
        elif k > k_index:
            return self.select(high, k - k_index - 1)
        else:
            return pivot

    def median(self, sublist):
        sublist.sort()
        mid = len(sublist) // 2
        return sublist[mid] if len(sublist) % 2 != 0 else (sublist[mid - 1] + sublist[mid]) / 2

# Example usage:
# mom = MedianOfMedians()
# result = mom.select([3, 1, 2, 5, 4], 2)  # Finds the 3rd smallest element (0-indexed)
# print(result)  # Output: 3