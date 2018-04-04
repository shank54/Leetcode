class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = x
        res = 0
        while l<=r:
            m = l+(r-l)/2
            if m <= x/m:
                l = m+1
                res = m
            else:
                r = m -1
        return res