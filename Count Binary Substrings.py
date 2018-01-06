class Solution(object):
    def countBinarySubstrings(self, s):
        c = 1
        l = []
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                c += 1
            else:
                l.append(c)
                c = 1
        l.append(c)
        s = 0
        for i in range(1,len(l)):
            s += min(l[i-1],l[i])
        return s