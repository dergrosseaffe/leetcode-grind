class TrieNode:

    def __init__(self, ):
        self.children = {}
        self.is_ending = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_ending = True


    def search(self, word: str) -> bool:
        nodes = [(self.root, 0)]

        while nodes:
            node, index = nodes.pop()

            if index == len(word):
                if node.is_ending:
                    return True
                continue

            char = word[index]
            if char == '.':
                for child in node.children:
                    nodes.append((node.children[child], index + 1))
            else:
                if char in node.children:
                    nodes.append((node.children[char], index + 1))

        return False
