class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = 0
        k = 0
        while i<len(g) and k<len(s):
            if g[i]<=s[k]:
                i += 1
            k += 1
        return i
                    
                    