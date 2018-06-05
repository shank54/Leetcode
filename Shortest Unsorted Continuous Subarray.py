class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        tmp = nums[:]
        tmp.sort()
        if tmp == nums:
            return 0
        for i in range(len(tmp)):
            if nums[i] != tmp[i]:
                flag = 1
                break
        start = i
        for i in range(len(tmp)-1,-1,-1):
            if nums[i] != tmp[i]:
                flag = 1
                break
        end = i
        return end-start+1