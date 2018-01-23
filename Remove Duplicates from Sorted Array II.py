class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in nums:
            if j<2 or i!=nums[j-2]:
                nums[j] = i
                j += 1
        return j