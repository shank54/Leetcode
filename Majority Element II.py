class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i] += 1
        print d
        res = []
        for i in d:
            if d[i]>len(nums)/3:
                res.append(i)
        return res