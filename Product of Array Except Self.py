class Solution(object):
    def productExceptSelf(self, nums):
        a = list()
        b = list()
        a.append(1)
        s = 1
        for i in range(1,len(nums)):
            s *= nums[i-1]
            a.append(s)
        s = 1
        n = len(nums)-1
        b.append(1)
        while n>0:
            s *= nums[n]
            n -= 1
            b.append(s)
        b = b[::-1]
        c = [0]*len(nums)
        for i in range(len(nums)):
            c[i] = a[i]*b[i]
        return c
        