class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        nums.sort()
        res = 0
        d = 0
        for i in range(len(nums)-1):
            d = nums[i+1]-nums[i]
            if d>res:
                res = nums[i+1]-nums[i]
        return res
        