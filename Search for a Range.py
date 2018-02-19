class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = []
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        if len(l)==0:
            return [-1,-1]
        if len(l)==1:
            return [l[0],l[0]]
        else:
            return [l[0],l[-1]]