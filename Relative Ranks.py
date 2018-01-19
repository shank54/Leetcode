class Solution(object):
    def findRelativeRanks(self, nums):
        a = nums[:]
        a.sort(reverse=True)
        d = dict()
        for i in range(len(a)):
            if i==0:
                d[a[i]] = "Gold Medal"
            elif i==1:
                d[a[i]] = "Silver Medal"
            elif i==2:
                d[a[i]] = "Bronze Medal"
            else:
                d[a[i]] = str(i+1)
        b = list()
        for i in nums:
            if i in d:
                b.append(d[i])
        return b