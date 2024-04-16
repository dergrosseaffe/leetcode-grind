class Solution:
    def trap(self, heights: List[int]) -> int:
        left_max = list(itertools.accumulate(heights, max))
        right_max = list(itertools.accumulate(reversed(heights), max))[::-1]

        trapped_water = 0
        for i in range(len(heights)):
            trapped_water += min(left_max[i], right_max[i]) - heights[i]

        return trapped_water
