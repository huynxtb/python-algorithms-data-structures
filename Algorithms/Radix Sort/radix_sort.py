class RadixSort:
    def sort(self, arr):
        max1 = max(arr) if arr else 0
        exp = 1
        while max1 // exp > 0:
            self._counting_sort(arr, exp)
            exp *= 10
        return arr

    def _counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1

        for i in range(n):
            arr[i] = output[i]