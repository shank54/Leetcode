class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        temp = 0
        while start<end:
            temp = numbers[start]+numbers[end]
            if temp == target:
                return [start+1,end+1]
            elif temp>target:
                end -= 1
            else:
                start += 1
        