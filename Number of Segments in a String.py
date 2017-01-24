class Solution(object):
    def countSegments(self, s):
        c = 0
        if s=="":
            return 0
        if s[0]!=" ":
                c += 1
        for i in range(1,len(s)):
            if s[i-1]==" " and s[i]!=" ":
                c += 1
        return c