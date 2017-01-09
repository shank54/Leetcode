class Solution(object):
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        else:
            dp = [0]*len(nums)
            dp[-1] = nums[len(nums)-1]
            dp[-2] = nums[len(nums)-2]
            i=len(nums)-3
            while i>=0 :
                dp[i] = nums[i]+ max(dp[i+2:])
                i-=1
            return max(dp)