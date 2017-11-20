class Solution(object):
    def hasAlternatingBits(self, n):
        a = [1,2,5,0]
        if n%10 not in a:
            return False
        b = bin(n)[2:]
        for i in range(1,len(b)):
            if b[i] == b[i-1]:
                return False
        return True
        