class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # builds a dictionary of words to other same-length words that are 1-edit distance
        # O(M^2 * N) where M is the length of each word and N is the number of words in wordList
        one_distance = defaultdict(list)
        words = wordList + [beginWord]
        num_words = len(words)
        for i in range(num_words):
            keyword = words[i]
            for j in range(i + 1, num_words):
                word = words[j]
                count = 0
                for k in range(len(beginWord)):
                    if keyword[k] != word[k]:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    one_distance[keyword].append(word)
                    one_distance[word].append(keyword)


        # tries to reach endWord from beginWord using one_distance entries
        # in bfs fashion
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            source, distance = queue.popleft()

            if source == endWord:
                return distance

            if source in visited:
                continue

            visited.add(source)

            for word in one_distance[source]:
                if word not in visited:
                    queue.append((word, distance + 1))

        return 0

