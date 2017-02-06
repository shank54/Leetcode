class Solution(object):
    def intersection(self, nums1, nums2):
        d1 = dict()
        d2 = dict()
        l = list()
        for i in nums1:
            d1.setdefault(i,0)
            d1[i] += 1
        
        for i in nums2:
            d2.setdefault(i,0)
            d2[i] += 1
        
        k = dict()
        k = {x:d1 for x in d1 if x in d2}
        for i in k:
            l.append(i)
        return l
