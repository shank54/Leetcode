class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        d = dict()
        for i in nums:
            d.setdefault(i,0)
            d[i] += 1
        m = 0
        x = 0
        for i in d:
            c = 0
            if i-1 not in d:
                x = i-1
                while x+1 in d:
                    c += 1
                    x += 1
            m = max(m,c)
        return m