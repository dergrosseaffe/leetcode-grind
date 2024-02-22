class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        longest_palindrome = 0
        can_add_center_char = True
        for count in counter.values():
            longest_palindrome += (count // 2) * 2

            # check for possibility of adding a center char
            if can_add_center_char and count % 2 == 1:
                longest_palindrome += 1
                can_add_center_char = False

        return longest_palindrome
