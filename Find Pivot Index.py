class Solution(object):
    def pivotIndex(self, nums):
        a = [0]*len(nums)
        b = [0]*len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            a[i] = s
        s = 0
        for i in xrange(len(nums)-1,-1,-1):
            s += nums[i]
            b[i] = s
        
        for i in range(len(a)):
            if a[i] == b[i]:
                return i
        return -1