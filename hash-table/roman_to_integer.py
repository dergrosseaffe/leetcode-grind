class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        sum = 0
        previous_value = 0
        for c in reversed(s):
            value = roman_to_int[c]
            sum += value if value >= previous_value else -value
            previous_value = value

        return sum
        