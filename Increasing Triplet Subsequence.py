class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        firstsmall = float('inf')
        secondsmall = float('inf')
        for i in nums:
            if i <= firstsmall:
                firstsmall = i
            elif i<=secondsmall:
                secondsmall = i
            else:
                return True
        return False