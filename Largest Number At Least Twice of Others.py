class Solution(object):
    def dominantIndex(self, nums):
        maxnum = 0
        maxnumindx = 0
        for i in range(len(nums)):
            if nums[i]>maxnum:
                maxnum = nums[i]
                maxnumindx = i
        for i in range(len(nums)):
            if maxnum!=nums[i] and nums[i]!=0 and maxnum/nums[i]<2:
                return -1
        return maxnumindx