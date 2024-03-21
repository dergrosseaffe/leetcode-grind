class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)

        for word in words:
            counts[word] -= 1

        maxheap = [(count, word) for word, count in counts.items()]

        heapq.heapify(maxheap)
        return [heapq.heappop(maxheap)[1] for _ in range(k)]
