class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1*(1.00000)
        if n<0:
            if n%2==0:
                t = float(self.myPow(x,n/2))
                return float((t*t))
            elif n%2!=0:
                m = float(1/x*(self.myPow(x,n+1)))
                return m
        if n>0:
            if n%2==0:
                t = float(self.myPow(x,n/2))
                return float(t*t)
            elif n%2!=0:
                m = float(x*(self.myPow(x,n-1)))
                return m
        