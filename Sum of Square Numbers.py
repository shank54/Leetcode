class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = int(c**(0.5))
        while a>=0:
            b = c-(a*a)
            s = int(b**(0.5))
            if s*s == b:
                return True
            a -= 1
        return False