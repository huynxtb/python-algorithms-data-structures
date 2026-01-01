class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, pattern: str) -> bool:
        def dfs(node, i):
            if i == len(pattern):
                return node.is_end_of_word

            char = pattern[i]

            if char == '?':
                for child_char, child_node in node.children.items():
                    if dfs(child_node, i + 1):
                        return True
                return False
            else:
                if char in node.children:
                    return dfs(node.children[char], i + 1)
                else:
                    return False

        return dfs(self.root, 0)