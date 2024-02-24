class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        if len(s) == 1: return s

        def palindromeSize(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1

            return right - left - 1

        longest = ""
        for i in range(len(s)-1):
            odd  = palindromeSize(i, i)
            even = palindromeSize(i, i+1)
            size = max(odd, even)

            if size > len(longest):
                left  = i - (size-1)//2  # adjust left index
                right = size//2 + i + 1  # adjust right index
                longest = s[left:right]

        return longest
