class Solution(object):
    def uniquePaths(self, m, n):
        c = [[0 for x in range(n)] for y in range(m)]
        # set first row to 1's
        for i in range(n):
            c[0][i] = 1
        # set first col to 1's
        for i in range(m):
            c[i][0] = 1
        # current = upper val + left val
        for i in range(1,m):
            for j in range(1,n):
                c[i][j] = c[i-1][j] + c[i][j-1]
        return c[m-1][n-1]