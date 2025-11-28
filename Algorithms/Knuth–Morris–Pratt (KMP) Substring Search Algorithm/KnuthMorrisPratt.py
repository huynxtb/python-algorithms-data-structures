def build_lps(pattern):
    """
    Build the Longest Prefix Suffix (LPS) array used to skip characters while matching.

    Args:
        pattern (str): The pattern string for which the LPS array is built.

    Returns:
        list[int]: LPS array where lps[i] is the length of the longest
                   proper prefix of pattern[:i+1] which is also a suffix of pattern[:i+1].
    """
    lps = [0] * len(pattern)  # LPS array initialization
    length = 0  # length of the previous longest prefix suffix
    i = 1

    # Loop through pattern starting from second character
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Consider previous longest prefix suffix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP substring search to find occurrences of pattern in text.

    Args:
        text (str): The text string to search within.
        pattern (str): The pattern string to search for.

    Returns:
        list[int]: Starting indices of all occurrences of pattern in text.
    """
    if not pattern:
        return []  # Edge case: empty pattern matches nowhere

    lps = build_lps(pattern)
    result_indices = []

    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # Full match of pattern found
            if j == len(pattern):
                result_indices.append(i - j)
                j = lps[j - 1]  # Continue searching
        else:
            if j != 0:
                j = lps[j - 1]  # Use LPS to avoid unnecessary comparisons
            else:
                i += 1

    return result_indices
