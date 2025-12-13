class SuffixTrie:
    class _Node:
        __slots__ = ['children']

        def __init__(self):
            # Children is a dict mapping char to _Node
            self.children = {}

    def __init__(self, text: str):
        """
        Construct the suffix trie for the given text.
        """
        self._root = self._Node()
        self._text = text
        self._build_suffix_trie(text)

    def _build_suffix_trie(self, text: str) -> None:
        """
        Builds the suffix trie by inserting all suffixes of text.
        This leads to a trie containing all suffixes starting from each index.
        """
        for start_index in range(len(text)):
            current = self._root
            # Insert the suffix text[start_index:]
            for char in text[start_index:]:
                if char not in current.children:
                    current.children[char] = self._Node()
                current = current.children[char]

    def contains(self, pattern: str) -> bool:
        """
        Checks if the pattern exists as a substring in the original text.

        Args:
            pattern (str): The substring pattern to search for.

        Returns:
            bool: True if the pattern exists, False otherwise.
        """
        current = self._root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
