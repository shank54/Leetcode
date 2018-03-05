class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        d = dict()
        for i in range(m):
            for j in range(n):
                d.setdefault(i+j+1,[])
                d[i+j+1].append(matrix[i][j])
        res = []
        for i in d:
            if i%2!=0:
                k = d[i][::-1]
                res += k
            else:
                res += d[i]
        return res