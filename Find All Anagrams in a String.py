class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        ds = [0]*123
        dp = [0]*123
        res = []
        for i in p:
            dp[ord(i)] += 1
        for i in range(len(p)):
            ds[ord(s[i])] += 1
        if ds == dp:
            res.append(0)
        i = 1
        j = i+len(p)-1
        while j<len(s):
            ds[ord(s[i-1])] -= 1
            ds[ord(s[j])] += 1
            if ds == dp:
                res.append(i)
            i += 1
            j += 1
        return res