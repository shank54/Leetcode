class Solution(object):
    def findLHS(self, nums):
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i] += 1
        l = list(d.keys())
        l.sort()
        m = 0
        c = 0
        for i in range(1,len(l)):
            c = abs(l[i]-l[i-1])
            a = l[i]
            b = l[i-1]
            if c == 1:
                c = d[a]+d[b]
                if c>=m:
                    m = c
        return m
                
        