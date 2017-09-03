class Solution(object):
    def isHappy(self, n):
        d = list()
        while n != 1:
            d.append(n)
            a = 0
            b = 0
            while n>0:
                a = n%10
                b += a**2
                n = n/10
            n = b
            if n in d:
                return False
        return True
        
        