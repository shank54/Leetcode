class Solution(object):
    def longestPalindrome(self, s):
        d = dict()
        if len(s)==0:
            return 0
        a = s[::-1]
        if s==a:
            return len(s)
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        c = 0
        y = 0
        for i in d:
            if d[i]>=1:
                if d[i]%2==0:
                    c += d[i]
                if d[i]%2!=0:
                    y += 1
                    c += d[i]-1
        if y==0:
            return c
        else:
            return c+1