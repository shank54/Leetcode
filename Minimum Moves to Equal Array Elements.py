class Solution(object):
    def minMoves(self, nums):
        m = sys.maxint
        for i in range(len(nums)):
            if nums[i]<=m:
                m = nums[i]
        s = 0
        for i in range(len(nums)):
            s += abs(nums[i]-m)
        return s