class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        d = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        res = -float('inf')
        for i in range(1):
            for j in range(len(matrix[0])):
                d[i][j] = int(matrix[i][j])
                res = max(res,d[i][j])
                
        for i in range(1):
            for j in range(len(matrix)):
                d[j][i] = int(matrix[j][i])
                res = max(res,d[j][i])
                
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]!="0":
                    d[i][j] = 1 + min(int(d[i-1][j]),int(d[i][j-1]),int(d[i-1][j-1]))
                res = max(res,d[i][j])
        
        return res*res