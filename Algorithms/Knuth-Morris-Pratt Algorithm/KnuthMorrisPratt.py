class KMP:
    @staticmethod
    def compute_lps(pattern: str) -> list:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    @staticmethod
    def search(text: str, pattern: str) -> list:
        if not pattern or not text or len(pattern) > len(text):
            return []
        lps = KMP.compute_lps(pattern)
        indices = []
        i = 0
        j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                indices.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return indices
