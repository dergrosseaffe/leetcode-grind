import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dp = defaultdict(list)
        alreadySeen = set()
        heap = []

        for px, py in points:
            dist = math.sqrt(px*px + py*py)
            dp[dist].append((px, py))

            if dist not in alreadySeen:
                heappush(heap, dist)
                alreadySeen.add(dist)

        r = []
        while k > 0 and heap:
            d = heapq.heappop(heap)
            r.extend(dp[d][:k])  # Makes sure not to exceed k points
            k -= len(dp[d])

        return r
