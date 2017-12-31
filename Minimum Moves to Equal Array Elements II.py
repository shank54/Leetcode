class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        c = 0
        i = 0
        j = len(nums)-1
        while i<j:
            c += nums[j]-nums[i]
            i += 1
            j -= 1
        return c
        