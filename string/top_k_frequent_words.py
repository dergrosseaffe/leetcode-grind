class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        counts = defaultdict(int)

        for word in words:
            counts[word] -= 1

        return [word for word, count in sorted(counts.items(), key=lambda i: i[1])[:k]]
