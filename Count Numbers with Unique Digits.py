class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        res = 10
        s = 9
        for i in range(2,n+1):
            if i>10:
                break
            s *= (9-i+2)
            res += s
        return res