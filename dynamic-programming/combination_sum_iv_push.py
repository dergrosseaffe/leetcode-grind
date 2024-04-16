class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        # push DP
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i+num] += dp[i]

        return dp[-1]
