from math import exp
class Solution(object):
    def trailingZeroes(self, n):
        if n<2:
            return 0
        else:
            return (n/5)+self.trailingZeroes(n/5)