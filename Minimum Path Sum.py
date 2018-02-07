class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        c = [[0 for x in range(n)] for y in range(m)]
        c[0][0] = grid[0][0]
        s = 0
        for i in range(n):
            s += grid[0][i]
            c[0][i] = s
        c[0][n-1] = s
        s = 0
        for i in range(m):
            s += grid[i][0]
            c[i][0] = s
        c[m-1][0] = s
        for i in range(1,m):
            for j in range(1,n):
                c[i][j] = grid[i][j]+min(c[i-1][j],c[i][j-1])
        return c[m-1][n-1]
        