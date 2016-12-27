class Solution(object):
    def containsDuplicate(self, nums):
        l = len(nums)
        a = list(set(nums))
        b = len(a)
        if b==l:
            return False
        return True