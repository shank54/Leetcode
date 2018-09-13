from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.ret = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ret
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if len(self.nums)<2:
            return self.nums
        a = randint(0,len(self.nums)-1)
        b = randint(0,len(self.nums)-1)
        self.nums[a],self.nums[b] = self.nums[b],self.nums[a]
        return self.nums
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()