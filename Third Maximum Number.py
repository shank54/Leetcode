class Solution(object):
    def thirdMax(self, nums):
        a = list(set(nums))
        l = len(a)
        b = sorted(a, reverse=True)
        if l>2:
            return b[2]
        return b[0]