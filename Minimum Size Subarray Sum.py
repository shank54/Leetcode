class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        l = float('inf')
        ans = 0
        while i<len(nums) and j<len(nums):
            ans += nums[j]
            while ans>=s:
                l = min(l,j-i+1)
                ans -= nums[i]
                i += 1
            j += 1
        if l==float('inf'):
            return 0
        return l