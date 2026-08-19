def rabin_karp(text: str, pattern: str, prime: int = 101, base: int = 256) -> list[int]:
    """
    Searches for all occurrences of a pattern in a text using the Rabin-Karp algorithm.

    Args:
        text: The string to search within.
        pattern: The string pattern to search for.
        prime: A prime number used for hashing (default: 101).
        base: The alphabet size or base used for hashing (default: 256).

    Returns:
        A list of 0-based starting indices where the pattern matches the text.
    """
    n = len(text)
    m = len(pattern)
    indices = []

    if m == 0 or n < m:
        return indices

    # Calculate h = (base ** (m - 1)) % prime
    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime

    p_hash = 0
    t_hash = 0

    # Calculate the initial hash values for pattern and first window of text
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        t_hash = (base * t_hash + ord(text[i])) % prime

    # Slide the pattern over text
    for i in range(n - m + 1):
        # Check if hash values match
        if p_hash == t_hash:
            # Verify characters to handle hash collisions
            if text[i : i + m] == pattern:
                indices.append(i)

        # Calculate hash value for the next window
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return indices