class Solution(object):
    def maxSlidingWindow(self, nums, k):
        maxnum = 0
        l = []
        print len(nums)
        for i in range(len(nums)):
            if i+k-1<len(nums):
                arr = nums[i:i+k]
                maxnum = max(arr)
                l.append(maxnum)
        return l
        