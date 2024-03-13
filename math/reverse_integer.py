class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        result *= sign

        return result if MIN <= result <= MAX else 0
