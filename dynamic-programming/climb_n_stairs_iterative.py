class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n <= 2:
            return n

        previous    = 2
        before_that = 1
        ways        = 0
        for _ in range(2, n):
            ways        = previous + before_that
            before_that = previous
            previous    = ways

        return ways
