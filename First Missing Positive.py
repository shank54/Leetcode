class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        res = [0]*(l+1)
        for i in nums:
            if i>0 and i<len(res):
                res[i] = 1
        flag = len(res)
        for i in range(1,len(res)):
            if res[i]==0:
                flag = i
                break
        return flag