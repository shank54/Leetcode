class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = [0]*len(nums)
        l = [0]*len(nums)
        s = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                s += 1
            else:
                s = 0
            r[i] = s
        s = 0
        i = len(nums)-1
        while i>=0:
            if nums[i] != 0:
                s += 1
            else:
                s = 0
            l[i] = s
            i -= 1
        m = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                s = 1
                if i-1>=0:
                    s += r[i-1]
                if i+1<len(nums):
                    s += l[i+1]
            m = max(m,s)
        return m