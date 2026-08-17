# Huffman Coding

## Introduction

Huffman Coding is a lossless data compression algorithm. It works by assigning variable-length codes to input characters, with lengths based on the frequencies of corresponding characters. More frequent characters get shorter codes, and less frequent characters get longer codes. This leads to a reduction in the overall size of the data when represented in binary.

It is particularly useful for compressing data where certain characters or symbols appear much more frequently than others, such as text files, images, and other forms of digital information.

## Usage


# Example Usage:

huffman = HuffmanCoding()

# Encode a string
original_string = "this is an example for huffman encoding"
encoded_data, code_map = huffman.encode(original_string)

print(f"Original String: {original_string}")
print(f"Encoded Data: {encoded_data}")
print(f"Code Map: {code_map}")

# Decode the binary string back to the original
decoded_string = huffman.decode(encoded_data, code_map)
print(f"Decoded String: {decoded_string}")

# Example with a single unique character
single_char_string = "aaaaa"
encoded_single, code_map_single = huffman.encode(single_char_string)
print(f"\nOriginal String (single char): {single_char_string}")
print(f"Encoded Data (single char): {encoded_single}")
print(f"Code Map (single char): {code_map_single}")
decoded_single = huffman.decode(encoded_single, code_map_single)
print(f"Decoded String (single char): {decoded_single}")

# Example with an empty string
empty_string = ""
encoded_empty, code_map_empty = huffman.encode(empty_string)
print(f"\nOriginal String (empty): '{empty_string}'")
print(f"Encoded Data (empty): '{encoded_empty}'")
print(f"Code Map (empty): {code_map_empty}")
decoded_empty = huffman.decode(encoded_empty, code_map_empty)
print(f"Decoded String (empty): '{decoded_empty}'")


## Detailed Explanation

### `HuffmanNode` Class

-   **Purpose:** Represents a node within the Huffman tree. Each node can either be a leaf node (representing a character) or an internal node (representing a combination of characters).
-   **Attributes:**
    -   `char`: The character stored in the node. It's `None` for internal nodes.
    -   `freq`: The frequency count of the character (for leaf nodes) or the sum of frequencies of its children (for internal nodes).
    -   `left`: A reference to the left child node.
    -   `right`: A reference to the right child node.
-   **`__lt__` and `__eq__`:** These methods are crucial for the `heapq` module to correctly order `HuffmanNode` objects based on their frequencies in the priority queue.

### `HuffmanCoding` Class

-   **`__init__`:** Initializes the Huffman coding instance with `root`, `codes` (character to binary code map), and `reverse_codes` (binary code to character map) attributes.

-   **`_build_frequency_map(text)`:**
    -   Takes an input string `text`.
    -   Uses `collections.Counter` to efficiently count the occurrences of each character.
    -   Returns a dictionary where keys are characters and values are their frequencies.
    -   Handles empty strings by returning an empty dictionary.

-   **`_build_huffman_tree(freq_map)`:**
    -   Takes the `freq_map` generated previously.
    -   Initializes a min-heap (priority queue) using `heapq`.
    -   For each character-frequency pair, it creates a `HuffmanNode` and pushes it onto the heap.
    -   **Edge Case (Single Unique Character):** If there's only one unique character, it creates a dummy parent node to ensure a valid tree structure for code generation.
    -   It repeatedly extracts the two nodes with the lowest frequencies from the heap.
    -   A new internal node is created with these two nodes as children, and its frequency is the sum of its children's frequencies.
    -   This new internal node is pushed back onto the heap.
    -   This process continues until only one node remains in the heap, which is the root of the Huffman tree.
    -   Returns the root node or `None` if the frequency map was empty.

-   **`_generate_binary_code_map(node, current_code)`:**
    -   This is a recursive helper method to traverse the Huffman tree and build the code map.
    -   It starts from the `root` node.
    -   When traversing to the left child, '0' is appended to the `current_code`.
    -   When traversing to the right child, '1' is appended.
    -   When a leaf node (a node with a `char`) is reached, the `current_code` accumulated is stored in the `self.codes` dictionary for that character. For the single character case, it assigns '0'.
    -   The `self.reverse_codes` map is also populated simultaneously.

-   **`encode(text)`:**
    -   The main public method for encoding.
    -   Handles empty input strings.
    -   Calls `_build_frequency_map` to get character frequencies.
    -   Calls `_build_huffman_tree` to construct the tree.
    -   Calls `_generate_binary_code_map` to populate the `codes` and `reverse_codes` dictionaries.
    -   Iterates through the input `text`, looks up the Huffman code for each character in `self.codes`, and concatenates them to form the `encoded_text`.
    -   Returns the `encoded_text` (a binary string) and the `codes` map.

-   **`decode(encoded_text, codes)`:**
    -   The main public method for decoding.
    -   Handles empty input `encoded_text` or `codes` map.
    -   It first reconstructs the `reverse_codes` map from the provided `codes` map for efficient lookup.
    -   It iterates through the `encoded_text` bit by bit.
    -   It builds `current_code` by appending bits.
    -   When `current_code` matches a key in `reverse_codes`, it means a character has been successfully decoded. The corresponding character is appended to `decoded_text`, and `current_code` is reset.
    -   Returns the `decoded_text`.

## Complexity Analysis

Let N be the number of characters in the input string and K be the number of unique characters.

### `_build_frequency_map`
-   **Time Complexity:** O(N) - Each character in the string is processed once.
-   **Space Complexity:** O(K) - To store the frequency of each unique character.

### `_build_huffman_tree`
-   **Time Complexity:** O(K log K) - Building the initial heap takes O(K log K). The `while` loop runs K-1 times, and each `heappop` and `heappush` operation takes O(log K) time.
-   **Space Complexity:** O(K) - To store the nodes in the priority queue and the tree itself.

### `_generate_binary_code_map`
-   **Time Complexity:** O(K) - Each node in the Huffman tree (which has at most 2K-1 nodes) is visited once.
-   **Space Complexity:** O(K) - To store the generated codes for each unique character.

### `encode`
-   **Time Complexity:** O(N + K log K) - Dominated by building the frequency map (O(N)) and constructing the tree (O(K log K)). The final encoding step takes O(N) because each character lookup and concatenation is effectively constant time on average for typical string implementations, or O(N * L_avg) where L_avg is the average code length if string concatenation is O(length).
-   **Space Complexity:** O(K) - For storing the frequency map, the Huffman tree, and the code map.

### `decode`
-   **Time Complexity:** O(M) - Where M is the length of the `encoded_text`. Each bit is processed once. The lookup in `reverse_codes` is O(1) on average.
-   **Space Complexity:** O(K) - To store the `reverse_codes` map. The `decoded_text` can grow up to O(N) in size.
