class Solution(object):
    def twoSum(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
            else:
                return [d[nums[i]],i]
        