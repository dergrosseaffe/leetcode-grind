class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0

        for value in range(1, amount + 1):
            for denomination in coins:
                if value - denomination >= 0:
                    memo[value] = min(memo[value], memo[value - denomination] + 1)

        return memo[amount] if memo[amount] != amount + 1 else -1
