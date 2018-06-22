class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return k
        d = [0]*(n+1)
        d[0] = 0
        d[1] = k
        s = [0]*(n+1)
        s[0] = 0
        s[1] = 1
        res = [0]*(n+1)
        for i in range(2,n+1):
            d[i] = (d[i-1]+d[i-2])*(k-1)
            s[i] = d[i-1]
            res[i] = s[i]+d[i]
        return res[n]
            