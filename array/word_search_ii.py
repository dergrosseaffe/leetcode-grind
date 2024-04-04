class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_ending = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_ending = True

    def search(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                return False, False
            node = node.children[char]

        return True, node.is_ending

    def remove(self, word: str) -> None:
        _, is_ending = self.search(word)

        if not is_ending:
            return

        stack = []
        node = self.root
        for char in word:
            stack.append((char, node))  # save current char and parent for later removal
            node = node.children[char]

        can_remove = not node.children

        while stack and can_remove:
            char, parent = stack.pop()
            if can_remove:
                del parent.children[char]

            can_remove = not parent.children and not parent.is_ending

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        # add all search words to trie
        trie = Trie()
        for word in words:
            trie.add(word)

        moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def safe(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def search(row, col, prefix, search_path):
            result, is_ending = trie.search(prefix)
            if result:
                # add word to found list
                if is_ending:
                    found_words.add(prefix)
                    trie.remove(prefix)

                for dx, dy in moves:
                    x, y = row + dx, col + dy
                    if safe(x, y) and (x, y) not in search_path:
                        if search(x, y, prefix + str(board[x][y]), search_path + [(x, y)]):
                            return True

            return False

        found_words = set()
        for row in range(rows):
            for col in range(cols):
                prefix = str(board[row][col])
                # starts search
                search(row, col, prefix, [(row, col)])

        return found_words
