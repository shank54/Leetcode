class Solution(object):
    def countBits(self, num):
        b = list()
        for i in range(0,num+1):
            a = bin(i)[2:].count("1")
            b.append(a)
        return b