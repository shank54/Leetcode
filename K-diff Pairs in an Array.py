class Solution(object):
    def findPairs(self, nums, k):
        if k<0:
            return 0
        d = dict()
        c = 0
        for i in nums:
            if i not in d:
                if i+k in d:
                    c += 1
                if i-k in d:
                    c += 1
                d[i] = 1
            elif i in d and d[i]<2:
                d[i] += 1
                if k == 0:
                    c += 1
        return c
                