class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c = 0
        m = 0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            if c>m:
                m=c
            if nums[i]==0:
                c=0
        return m