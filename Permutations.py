class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.perm([],nums,res)
        return res
        
    def perm(self,pre,s,res):
        if not s:
            res.append(pre)
        for i in range(len(s)):
            (self.perm(pre+[s[i]],s[:i]+s[i+1:],res))