class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.m = len(pattern)
        self.bad_char = self.preprocess_bad_char()
        self.good_suffix = self.preprocess_good_suffix()

    def preprocess_bad_char(self):
        # Preprocessing for bad character rule
        bad_char = [-1] * 256  # considering ASCII character set
        for i in range(self.m):
            bad_char[ord(self.pattern[i])] = i
        return bad_char

    def preprocess_good_suffix(self):
        m = self.m
        pattern = self.pattern

        # preprocess border positions
        border_pos = [0] * (m + 1)
        shift = [0] * (m + 1)

        i = m
        j = m + 1
        border_pos[i] = j

        while i > 0:
            while j <= m and pattern[i - 1] != pattern[j - 1]:
                if shift[j] == 0:
                    shift[j] = j - i
                j = border_pos[j]
            i -= 1
            j -= 1
            border_pos[i] = j

        j = border_pos[0]
        for i in range(m + 1):
            if shift[i] == 0:
                shift[i] = j
            if i == j:
                j = border_pos[j]

        return shift

    def search(self, text):
        n = len(text)
        m = self.m
        bad_char = self.bad_char
        good_suffix = self.good_suffix

        occurrences = []
        s = 0  # shift of the pattern with respect to text
        while s <= n - m:
            j = m - 1

            while j >= 0 and self.pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                occurrences.append(s)
                s += good_suffix[0]
            else:
                bc_shift = j - bad_char[ord(text[s + j])] if bad_char[ord(text[s + j])] != -1 else j + 1
                gs_shift = good_suffix[j + 1]
                s += max(bc_shift, gs_shift)

        return occurrences