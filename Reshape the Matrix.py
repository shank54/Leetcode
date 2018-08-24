class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        r1 = len(nums)
        c1 = len(nums[0])
        if r1 == r and c1 == c:
            return nums
        if r1*c1 != r*c:
            return nums
        res = [[0 for j in range(c)] for i in range(r)]
        temp = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                temp.append(nums[i][j])
        k = 0
        for i in range(len(res)):
            j = 0
            while j<len(res[0]):
                res[i][j] = temp[k]
                k += 1
                j += 1
        return res