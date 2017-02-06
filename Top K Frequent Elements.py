class Solution(object):
    def topKFrequent(self, nums, k):
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i] += 1
        a = 0
        l = list()
        for w in sorted(d, key=d.get, reverse=True):
            a += 1
            if a<=k:
                l.append(w)
            else:
                break
        return l
        