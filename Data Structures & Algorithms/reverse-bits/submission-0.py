class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # res move left 1 bit
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res
        