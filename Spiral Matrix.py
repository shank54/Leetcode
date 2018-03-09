class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        t = 0
        b= m-1
        l = 0
        r = n-1
        d = 0
        res = []
        while t<=b and l<=r:
            if d==0:
                for i in range(l,r+1):
                    res.append(matrix[t][i])
                t += 1
                d = 1
            elif d == 1:
                for i in range(t,b+1):
                    res.append(matrix[i][r])
                r -= 1
                d = 2
            elif d == 2:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b -= 1
                d = 3
            elif d == 3:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l += 1
                d = 0
                
        return res
        