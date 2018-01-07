class Solution(object):
    def findShortestSubArray(self, nums):
        d = dict()
        l = dict()
        r = dict()
        for i in range(len(nums)):
            if nums[i] not in l:
                l[nums[i]] = i
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
            r[nums[i]] = i
        a = len(nums)
        m = max(d.values())
        for i in d:
            if d[i]==m:
                a = min(a,r[i]-l[i]+1)
                
        return a
        