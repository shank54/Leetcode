class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l + h)/2
            if nums[m]<target:
                l = m + 1
            elif nums[m]==target:
                return m
            else:
                h = m - 1
        return l