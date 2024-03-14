class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.is_ending = False


class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()


    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_ending = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_ending


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)

        memo = {}
        def has_solution(node: TrieNode, start_index: int) -> bool:
            if start_index == len(s):
                return True

            if start_index in memo:
                return memo[start_index]

            for i in range(start_index, len(s)):
                char = s[i]
                if char in node.children:
                    node = node.children[char]
                    if node.is_ending:
                        if has_solution(trie.root, i + 1):
                            memo[start_index] = True
                            return True
                else:
                    break

            memo[start_index] = False
            return False

        return has_solution(trie.root, 0)
