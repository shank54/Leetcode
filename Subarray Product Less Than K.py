class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        c = 0
        p = 1
        l = 0
        res = 0
        for i in range(len(nums)):
            p *= nums[i]
            while p>=k:
                p /= nums[l]
                l += 1
            res += i-l+1
        return res
            