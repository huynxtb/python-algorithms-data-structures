# Rabin-Karp String Matching Algorithm

### 1. Introduction
The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find any one of a set of pattern strings in a text. It is particularly useful for multiple pattern search and plagiarism detection.

### 2. Usage

# Example usage of the rabin_karp function
text = "ABCCDDAEFGBC"
pattern = "BC"
matches = rabin_karp(text, pattern)
print(matches)  # Output: [1, 10]


### 3. Detailed Explanation
The algorithm computes a hash value for the pattern and for each substring of the text of length $M$ (where $M$ is the pattern length). 
1. **Initial Hash**: Computes the hash of the pattern and the first window of the text in $O(M)$ time.
2. **Rolling Hash**: As the window slides one character to the right, the new hash value is calculated in $O(1)$ time by subtracting the contribution of the departing character and adding the contribution of the entering character.
3. **Collision Resolution**: If the hash values match, the algorithm performs a direct character-by-character comparison to rule out spurious hits (hash collisions).

### 4. Complexity Analysis
- **Time Complexity**:
  - **Best/Average Case**: $O(N + M)$, where $N$ is the length of the text and $M$ is the length of the pattern.
  - **Worst Case**: $O(N \cdot M)$, which occurs when there are many hash collisions (e.g., searching a pattern of all 'A's in a text of all 'A's).
- **Space Complexity**: $O(1)$ auxiliary space, as it only stores a few variables for hash values and indices.