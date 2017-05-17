class Solution(object):
    def maxSubArray(self, nums):
        a = 0
        b = float('-inf')
        if max(nums)<0:
            return max(nums)
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            a += nums[i]
            if a<0:
                a = 0
            if b<a:
                b = a
        return b