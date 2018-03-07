class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        d = dict()
        i = 0
        j = 0
        m = 0
        while i<n and j<n:
            if s[j] not in d:
                d[s[j]] = 1
                j += 1
                m = max(m,j-i)
            else:
                del d[s[i]]
                i += 1
        return m
        