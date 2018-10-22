class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n>0:
            n -= 1
            ans += chr(ord('A')+(n)%26)
            n = n/26
        return ans[::-1]