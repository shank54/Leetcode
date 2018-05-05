class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tmp = 1
        r = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                tmp += 1
            else:
                tmp = 1
            r = max(r,tmp)
        return r