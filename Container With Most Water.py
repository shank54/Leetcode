class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        a = 0
        tmp = 0
        while i<j:
            tmp = (j-i)*(min(height[i],height[j]))
            a = max(a,tmp)
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return a