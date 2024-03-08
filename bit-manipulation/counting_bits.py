class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n+1):
            s = 0
            while i > 0:
                s += (i) & 0b1
                i >>= 1
            bits.append(s)

        return bits
