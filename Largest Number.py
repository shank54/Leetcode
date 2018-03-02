class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        tmp = []
        for i in nums:
            tmp.append(str(i))
        l = (sorted(tmp, cmp=self.large))
        ans = "".join(l)
        return str(int(ans))
        
    def large(self,a,b):
        if int(str(a)+str(b))>int(str(b)+str(a)):
            return -1
        return 1