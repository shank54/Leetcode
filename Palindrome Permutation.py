class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = dict()
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        c = 0
        for i in d:
            if d[i]%2 != 0:
                c += 1
        if c<=1:
            return True
        else:
            return False