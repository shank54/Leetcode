class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # iterate over the array
        # create new list of inf's
        # if picked val is <= elem in list replace
        if not nums:
            return 0
        l = [float('inf')]*len(nums)
        l[0] = nums[0]
        for i in range(1,len(nums)):
            for j in range(len(l)):
                if nums[i]<=l[j]:
                    l[j] = nums[i]
                    break
                else:
                    continue
        c = 0
        for i in l:
            if i==float('inf'):
                break
            c += 1
        return c