class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        carry = 0

        result = ''
        while a > 0 or b > 0 or carry > 0:
            sum   = (a & 0b1) + (b & 0b1) + carry
            carry = sum // 2
            result = str(sum % 2) + result

            a >>= 1
            b >>= 1

        return result if result else '0'
