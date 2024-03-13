class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def minCoins(currentAmount: int):
            if currentAmount < 0:
                return float('+inf')

            if currentAmount == 0:
                return 0

            if currentAmount in cache:
                return cache[currentAmount]

            best = float('+inf')
            for denomination in coins:
                best = min(best, minCoins(currentAmount - denomination) + 1)

            cache[currentAmount] = best
            return best

        result = minCoins(amount)
        return result if result != float('+inf') else -1
