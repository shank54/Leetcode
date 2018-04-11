class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        ans = 0
        i = 2
        flag = 0
        while i*i <= n:
            if n%i == 0:
                ans += i
                flag = 1
                n = n/i
                i = 2
            else:
                i += 1
        if flag ==0:
            return n
        else:
            return ans+n