class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        j =0
        for i in range(0,l):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1

        