class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = bin(n)[2:].zfill(32)
        b = a[::-1].zfill(32)
        return int(b,2)