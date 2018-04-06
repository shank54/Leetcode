class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        # if fully sorted
        if nums[l]<=nums[r]:
            return nums[l]
        # only one ele or all are same
        if nums[l]==nums[r]:
            return nums[l]
        # rotated
        while l<=r:
            m = l+(r-l)/2
            if nums[m+1]<nums[m]:
                return nums[m+1]
            elif nums[m-1]>nums[m]:
                return nums[m]
            else:
                if nums[m]<nums[r]:
                    r = m-1
                else:
                    l = m+1