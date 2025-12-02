class SuffixArray:
    def __init__(self, text: str):
        self.text = text
        self.n = len(text)
        self.suffix_array = self.build_suffix_array(text)

    def build_suffix_array(self, s: str):
        # Using the O(n log n) suffix array construction algorithm based on sorting by 2^k substrings
        n = len(s)
        suffix_arr = list(range(n))
        rank = [ord(c) for c in s] + [-1]  # rank array for characters, -1 for bounds
        temp_rank = [0] * n
        k = 1

        def suffix_cmp(i, j):
            if rank[i] != rank[j]:
                return rank[i] - rank[j]
            ri = rank[i + k] if (i + k < n) else -1
            rj = rank[j + k] if (j + k < n) else -1
            return ri - rj

        # We sort suffixes by first character initially, then by first 2 chars, then 4, 8...
        while k < n:
            suffix_arr.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

            temp_rank[suffix_arr[0]] = 0
            for i in range(1, n):
                temp_rank[suffix_arr[i]] = temp_rank[suffix_arr[i - 1]] + (suffix_cmp(suffix_arr[i - 1], suffix_arr[i]) < 0)

            rank, temp_rank = temp_rank, rank
            k <<= 1

        return suffix_arr

    def get_suffix_array(self):
        return self.suffix_array

    def compare_suffixes(self, i: int, j: int) -> int:
        """
        Lexicographically compare suffix starting at index i and suffix starting at index j.
        Returns:
            - Negative if suffix at i < suffix at j
            - Zero if suffix at i == suffix at j
            - Positive if suffix at i > suffix at j
        """
        n = self.n
        s = self.text
        while i < n and j < n:
            if s[i] != s[j]:
                return ord(s[i]) - ord(s[j])
            i += 1
            j += 1
        # If one suffix is a prefix of the other, shorter suffix is lex smaller
        return (n - i) - (n - j)