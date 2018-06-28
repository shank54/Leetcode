class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0]*(length+1)
        for i in updates:
            start,end,inc = i
            res[start] += inc
            res[end+1] -= inc
        
        for i in range(1,len(res)):
            res[i] = res[i]+res[i-1]
        
        return res[:-1]