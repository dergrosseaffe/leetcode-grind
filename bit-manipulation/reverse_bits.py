class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r += (n >> i & 0b1) << (32 - i - 1)

        return r
