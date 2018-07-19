class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = [0]*(len(nums))
        i = 0
        j = len(nums)-1
        indx = 0
        if a>0:
            indx = len(nums)-1
        while i<=j:
            if a>0:
                if self.calc(nums[i],a,b,c) > self.calc(nums[j],a,b,c):
                    res[indx] = self.calc(nums[i],a,b,c)
                    i += 1
                else:
                    res[indx] = self.calc(nums[j],a,b,c)
                    j -= 1
                indx -= 1
            else:
                if self.calc(nums[i],a,b,c) > self.calc(nums[j],a,b,c):
                    res[indx] = self.calc(nums[j],a,b,c)
                    j -= 1
                else:
                    res[indx] = self.calc(nums[i],a,b,c)
                    i += 1
                indx += 1
        return res
    
    def calc(self,x,a,b,c):
        return a*(x*x)+b*(x)+c
                