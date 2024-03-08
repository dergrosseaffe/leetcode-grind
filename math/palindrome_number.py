class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        # reverses and compares
        original = x
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10

        return original == y
