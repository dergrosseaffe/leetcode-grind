class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        maxLength = 0
        for c in s:
            if c in string:
                index = string.index(c)
                string = string[index+1:] + c
            else:
                string = string + c
            if (len(string) > maxLength):
                maxLength = len(string)

        return maxLength
