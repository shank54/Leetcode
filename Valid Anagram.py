class Solution(object):
    def isAnagram(self, s, t):
        d = dict()
        e = dict()
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        for i in t:
            e.setdefault(i,0)
            e[i] += 1
        return d==e