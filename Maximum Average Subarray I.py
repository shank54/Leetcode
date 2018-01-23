class Solution(object):
    def findMaxAverage(self, nums, k):
        res = []
        s = 0
        for i in range(k):
            s += nums[i]
        res.append(s/float(k))
        for i in range(k,len(nums)):
            s = s+nums[i]-nums[i-k]
            res.append(s/float(k))
        return max(res)
        