class Solution(object):
    def intersect(self, nums1, nums2):
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
        for i in d1:
            if i in d2:
                if d1[i]<=d2[i]:
                    k[i] = d1[i]
                else:
                    k[i] = d2[i]
        print k
        for i in k:
            l += k[i]*[i]
        return l
        