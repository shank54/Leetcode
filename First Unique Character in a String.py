class Solution(object):
    def firstUniqChar(self, s):
        d = dict()
        for i in range(len(s)):
            d.setdefault(s[i],0)
            d[s[i]] += 1
        a = list()
        for i in d:
            if d[i]==1:
                a.append(s.index(str(i)))
        if len(a)>=1:
            return min(a)
        else:
            return -1