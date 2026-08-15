# Lempel-Ziv-Welch (LZW) Compression

## 1. Introduction
Lempel-Ziv-Welch (LZW) is a universal, lossless data compression algorithm. It works by reading a sequence of symbols, grouping them into strings, and converting the strings into codes. The algorithm dynamically builds a translation dictionary during both compression and decompression, meaning the dictionary does not need to be transmitted with the compressed data. LZW is widely used in formats like GIF, TIFF, and PDF.

## 2. Usage

# Example usage of the LZW class
from lzw import LZW

original_text = "TOBEORNOTTOBEORTOBEORNOT"
compressed_data = LZW.compress(original_text)
print(f"Compressed: {compressed_data}")

decompressed_text = LZW.decompress(compressed_data)
print(f"Decompressed: {decompressed_text}")

assert original_text == decompressed_text


## 3. Detailed Explanation
- **Compression**: The dictionary is initialized with the 256 standard ASCII characters. The algorithm scans the input string for progressively longer substrings that exist in the dictionary. When a substring `W` is found but `W + next_character` is not, the code for `W` is output, and `W + next_character` is added to the dictionary with a new code.
- **Decompression**: The dictionary is initialized in the same way. The algorithm reconstructs the dictionary on the fly by reading the codes. For each code, it retrieves the corresponding string from the dictionary, outputs it, and adds the combination of the previous translation and the first character of the current translation to the dictionary. A special case occurs when a code is read that is not yet in the dictionary (e.g., `KwKkW` pattern); this is resolved by using the previous string concatenated with its own first character.

## 4. Complexity Analysis
- **Time Complexity**:
  - **Compression**: $O(N)$ where $N$ is the length of the input string, assuming dictionary lookups and insertions take $O(1)$ time on average.
  - **Decompression**: $O(M)$ where $M$ is the number of codes in the compressed list.
- **Space Complexity**:
  - **Compression**: $O(D)$ where $D$ is the number of unique substrings added to the dictionary.
  - **Decompression**: $O(D)$ to store the reconstructed dictionary.