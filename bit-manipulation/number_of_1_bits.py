class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            print(n)
            n &= n - 1  # Turn off the rightmost 1-bit
            count += 1
        return count
