class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        m = 0
        d = dict()
        while j<len(s) and i<len(s):
            for c in d.keys():
                if d[c] == 0:
                    del d[c]
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if len(d)<k+1:
                m = max(m,len(s[i:j+1]))
            j += 1
            if len(d)>k:
                if s[i] in d:
                    if d[s[i]] == 0:
                        del d[s[i]]
                    else:
                        d[s[i]] -= 1
                    i += 1
        return m