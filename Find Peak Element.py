class Solution(object):
    def findPeakElement(self, nums):
        m = float('-inf')
        n=0
        for i in range(len(nums)):
            if nums[i]>m:
                m = nums[i]
                n = i
        return n