import heapq
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple, Any

class HuffmanNode:
    """Represents a node in the Huffman tree.

    Attributes:
        char (Optional[str]): The character represented by this node. None for internal nodes.
        freq (int): The frequency of the character or the sum of frequencies of its children.
        left (Optional[HuffmanNode]): The left child node.
        right (Optional[HuffmanNode]): The right child node.
    """
    def __init__(self, char: Optional[str], freq: int, left: Optional['HuffmanNode'] = None, right: Optional['HuffmanNode'] = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """Compares nodes based on frequency for priority queue ordering."""
        return self.freq < other.freq

    def __eq__(self, other: object) -> bool:
        """Checks for equality based on frequency and character."""
        if not isinstance(other, HuffmanNode):
            return NotImplemented
        return self.freq == other.freq and self.char == other.char

class HuffmanCoding:
    """Implements Huffman Coding for data compression.

    Provides methods to encode and decode strings using Huffman's algorithm.
    """

    def __init__(self):
        self.root: Optional[HuffmanNode] = None
        self.codes: Dict[str, str] = {}
        self.reverse_codes: Dict[str, str] = {}

    def _build_frequency_map(self, text: str) -> Dict[str, int]:
        """Builds a frequency map of characters in the input text.

        Args:
            text (str): The input string.

        Returns:
            Dict[str, int]: A dictionary mapping characters to their frequencies.
        """
        if not text:
            return {}
        return Counter(text)

    def _build_huffman_tree(self, freq_map: Dict[str, int]) -> Optional[HuffmanNode]:
        """Constructs the Huffman tree from a frequency map.

        Args:
            freq_map (Dict[str, int]): A dictionary mapping characters to their frequencies.

        Returns:
            Optional[HuffmanNode]: The root node of the Huffman tree, or None if the frequency map is empty.
        """
        if not freq_map:
            return None

        priority_queue: List[HuffmanNode] = []
        for char, freq in freq_map.items():
            heapq.heappush(priority_queue, HuffmanNode(char, freq))

        # Handle the edge case of a single unique character
        if len(priority_queue) == 1:
            node = heapq.heappop(priority_queue)
            # Create a dummy parent node to ensure a tree structure
            return HuffmanNode(None, node.freq, left=node)

        while len(priority_queue) > 1:
            left_child = heapq.heappop(priority_queue)
            right_child = heapq.heappop(priority_queue)

            merged_freq = left_child.freq + right_child.freq
            merged_node = HuffmanNode(None, merged_freq, left_child, right_child)
            heapq.heappush(priority_queue, merged_node)

        return heapq.heappop(priority_queue) if priority_queue else None

    def _generate_binary_code_map(self, node: Optional[HuffmanNode], current_code: str = ""):
        """Recursively generates the binary codes for each character.

        Args:
            node (Optional[HuffmanNode]): The current node in the Huffman tree.
            current_code (str): The binary code accumulated so far.
        """
        if node is None:
            return

        # If it's a leaf node, store the code
        if node.char is not None:
            self.codes[node.char] = current_code if current_code else '0' # Handle single character case
            self.reverse_codes[current_code if current_code else '0'] = node.char
            return

        # Traverse left (append '0')
        self._generate_binary_code_map(node.left, current_code + "0")
        # Traverse right (append '1')
        self._generate_binary_code_map(node.right, current_code + "1")

    def encode(self, text: str) -> Tuple[str, Dict[str, str]]:
        """Encodes a string using Huffman Coding.

        Args:
            text (str): The input string to encode.

        Returns:
            Tuple[str, Dict[str, str]]: A tuple containing the encoded binary string and the code map.
                                       Returns an empty string and empty map for empty input.
        """
        if not text:
            return "", {}

        freq_map = self._build_frequency_map(text)
        self.root = self._build_huffman_tree(freq_map)
        self.codes = {}
        self.reverse_codes = {}
        self._generate_binary_code_map(self.root)

        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text, self.codes

    def decode(self, encoded_text: str, codes: Dict[str, str]) -> str:
        """Decodes a Huffman encoded binary string back to the original string.

        Args:
            encoded_text (str): The binary string to decode.
            codes (Dict[str, str]): The Huffman code map used for encoding.

        Returns:
            str: The decoded original string. Returns an empty string if input is empty.
        """
        if not encoded_text or not codes:
            return ""

        # Rebuild reverse_codes map for efficient lookup during decoding
        reverse_codes: Dict[str, str] = {v: k for k, v in codes.items()}

        decoded_text = ""
        current_code = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_codes:
                decoded_text += reverse_codes[current_code]
                current_code = ""
        return decoded_text
