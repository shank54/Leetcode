class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        d = dict()
        for i in arr:
            d.setdefault(abs(x-i),[])
            d[abs(x-i)].append(i)
        res = []
        for i in sorted(d):
            res += d[i]
        ans = res[:k]
        ans.sort()
        return ans