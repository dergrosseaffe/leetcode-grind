class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i, max_jump in enumerate(nums):
            if not dp[i]:
                continue

            for jump in range(1, max_jump + 1):
                if (i + jump) >= len(nums) - 1:
                    return True

                dp[i + jump] = True

        return dp[-1]
