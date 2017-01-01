class Solution(object):
    def hammingDistance(self, x, y):
        c = bin(x^y)
        return c.count('1')