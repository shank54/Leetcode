class Solution(object):
    def countPrimeSetBits(self, L, R):
        bits = 0
        c = 0
        prime = {2,3,5,7,11,13,17,19}
        for i in range(L,R+1):
            bits = bin(i).count('1')
            if bits in prime:
                c += 1
        return c