class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        value = 0
        current = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if not s: return 0

        # process all leading spaces
        while current < len(s) and s[current] == ' ':
            current += 1

        # process leading - or + sign
        if current < len(s) and s[current] in ('+', '-'):
            sign = -1 if s[current] == '-' else 1
            current += 1

        for i in range(current, len(s)):
            c = s[i]

            if c.isdigit():
                c = int(c)
                # check for overflow/underflow before actually adding the digit
                if value > (INT_MAX - c) // 10:
                    return INT_MAX if sign == 1 else INT_MIN

                value = value * 10 + c
            else:
                break

        return max(-2 ** 31, min(2 ** 31 - 1, sign * value))
