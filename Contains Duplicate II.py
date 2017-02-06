class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        l = list()
        for i in range(len(nums)):
            d.setdefault(nums[i],[])
            d[nums[i]].append(i)
        
        for j in d  :
            l=d[j]
            for i in range(1,len(l)):
                if abs(l[i-1]-l[i])<=k:
                    return True
        return False
