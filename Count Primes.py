class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        bol = [False]*(n)
        i = 2
        c = 0
        while i<n:
            if bol[i] == False:
                c += 1
                for k in range(i,n,i):
                    bol[k] = True
            i += 1
        return c