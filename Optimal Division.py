class Solution(object):
    def optimalDivision(self, nums):
        s = ""
        if len(nums)==1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0])+"/"+str(nums[1])
        for i in range(len(nums)-1):
            if i == 1:
                s += "("
            s += str(nums[i])+"/"
        s += str(nums[-1])
        s += ")"
        return s