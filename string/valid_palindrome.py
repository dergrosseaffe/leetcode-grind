import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()

        for i, c in enumerate(s):
            if (c != s[len(s) - 1 - i]):
                return False
            if (i >= len(s)/2):
                return True

        return True
