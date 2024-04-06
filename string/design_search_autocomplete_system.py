class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_ending = False
        self.hot_degree = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def add(self, word: str, hot_degree: int) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_ending = True
        node.hot_degree += hot_degree


    def search(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]

        # if node.is_ending:
        #     node.hot_degree += 1
        return node


    def query(self, prefix: str) -> List[str]:
        node = self.search(prefix)
        if node:
            # builds a list of 3 hottest sentences from this node
            sentences = []
            queue = deque()
            queue.append((node, prefix))

            while queue:
                node, prefix = queue.popleft()

                if node.is_ending:
                    sentences.append((-node.hot_degree, prefix))

                for c in node.children:
                    queue.append((node.children[c], prefix + c))

            # heapify sentence list based on hot_degree and pulls
            # at most 3 elements
            return [v for k, v in heapq.nsmallest(3, sentences)]
        else:
            return []


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for sentence, hot_degree in zip(sentences, times):
            self.trie.add(sentence, hot_degree)
        self.query = ""


    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.query, 1) # hot degree is incremented, not updated
            self.query = ""
            return []
        else:
            self.query += c
            return self.trie.query(self.query)
