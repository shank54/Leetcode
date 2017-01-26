class Solution(object):
    def findDisappearedNumbers(self, nums):
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i]+=1
        l = list()
        for i in range(1,len(nums)+1):
            if i not in d:
                l.append(i)
        return l
        
        