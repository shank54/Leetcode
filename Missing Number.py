class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        a = (n*(n+1))/2
        s = 0
        for i in nums:
            s += i
        return a-s