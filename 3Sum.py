class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s==0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s>0:
                    r -= 1
                else:
                    l += 1
        return res