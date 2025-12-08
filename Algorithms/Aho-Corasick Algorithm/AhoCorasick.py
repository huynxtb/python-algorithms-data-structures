class AhoCorasick:
    class Node:
        __slots__ = ['children', 'fail', 'output']

        def __init__(self):
            self.children = {}  # char -> Node
            self.fail = None    # failure link
            self.output = []    # list of patterns ending at this node

    def __init__(self, keywords=None):
        """
        Initialize the Aho-Corasick automaton with an optional list of keywords.
        :param keywords: Optional list of lowercase strings to insert into the automaton.
        """
        self.root = self.Node()
        if keywords:
            for word in keywords:
                self.insert(word)
            self.build_failures()

    def insert(self, word):
        """
        Insert a keyword into the trie structure.
        :param word: A lowercase string to insert.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.output.append(word)

    def build_failures(self):
        """
        Construct the failure links using a BFS traversal.
        This prepares the automaton for efficient pattern matching.
        """
        from collections import deque
        queue = deque()

        # Initialize the fail link of root's children to root
        for ch, child in self.root.children.items():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()
            for ch, child in current.children.items():
                # Find fail state for child
                fail_state = current.fail
                while fail_state and ch not in fail_state.children:
                    fail_state = fail_state.fail
                child.fail = fail_state.children[ch] if fail_state and ch in fail_state.children else self.root
                # Append output of fail state to child's output
                child.output += child.fail.output
                queue.append(child)

    def search(self, text):
        """
        Search the text for all occurrences of the keywords stored in the automaton.
        :param text: The text string to search in.
        :return: A dictionary mapping each found keyword to a list of starting indices where it appears.
        """
        node = self.root
        results = {}

        for i, ch in enumerate(text):
            # Follow fail links if character not found
            while node and ch not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[ch]
            for pattern in node.output:
                if pattern not in results:
                    results[pattern] = []
                # i is the index of the last char of the pattern in the text
                results[pattern].append(i - len(pattern) + 1)

        return results
