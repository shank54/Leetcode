class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        i = 2
        s = 0
        n = int(num**(1/2.0))
        while i<=n:
            if num%i==0:
                s += i
                s +=(num/i) 
            i += 1
        return s==num-1
        