class Solution(object):
    def removeElement(self, nums, val):
        l = len(nums)
        for i in range(0,l):
            if val in nums:
                nums.remove(val)
        return len(nums)