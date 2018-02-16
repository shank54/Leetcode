class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in range(len(t)):
            if j<len(s) and t[i]==s[j]:
                j += 1
        if j==len(s):
            return True
        else:
            return False