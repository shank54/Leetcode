class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        mat = [[0 for x in range(n)] for y in range(n)]
        rlen = len(mat)
        clen = len(mat[0])
        t = 0
        b = rlen-1
        l = 0
        r = clen-1
        d = 0
        num = 1
        while t<=b and l<=r:
            if d == 0:
                for i in range(l,r+1):
                    mat[t][i] = num
                    num += 1
                t += 1
                d = 1
            elif d == 1:
                for i in range(t,b+1):
                    mat[i][r] = num
                    num += 1
                r -= 1
                d = 2
                
            elif d == 2:
                for i in range(r,l-1,-1):
                    mat[b][i] = num
                    num += 1
                b -= 1
                d = 3
            
            elif d == 3:
                for i in range(b,t-1,-1):
                    mat[i][l] = num
                    num += 1
                l += 1
                d = 0
        return mat
                    
                    