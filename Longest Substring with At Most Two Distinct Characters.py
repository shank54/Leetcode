class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        m = 0
        d = dict()
        while j<len(s) and i<len(s):
            for k in d.keys():
                if d[k] == 0:
                    del d[k]
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if len(d)<3:
                m = max(m,len(s[i:j+1]))
            j += 1
            if len(d)>2:
                if s[i] in d:
                    if d[s[i]] == 0:
                        del d[s[i]]
                    else:
                        d[s[i]] -= 1
                    i += 1
        return m