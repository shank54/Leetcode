class Solution(object):
    def singleNumber(self, nums):
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i] += 1
        for i in d:
            if d[i]==1:
                return i
        