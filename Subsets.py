class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums)):
            res.append([nums[i]])
            temp = []
            for j in range(1,len(res)-1):
                temp = res[j][:]
                temp.append(nums[i])
                res.append(temp)
        return res
        