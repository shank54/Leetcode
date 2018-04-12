class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        vis = dict()
        for i in range(len(nums)):
            c = 0
            prev = i
            if i not in vis:
                d = dict()
                while nums[i] not in d:
                    prev = nums[prev]
                    d[nums[prev]] = nums[prev]
                    vis.setdefault(nums[prev],0)
            m = max(len(d),m)
        return m