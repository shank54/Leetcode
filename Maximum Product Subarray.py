class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mx = nums[0]
        mn = nums[0]
        res = mx
        for i in nums[1:]:
            a = mx
            b = mn
            mx = max(i,i*a,i*b)
            mn = min(i,i*a,i*b)
            res=max(res, mx)
        return res