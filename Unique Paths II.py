class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        c = [[0 for x in range(n)] for y in range(m)]
        # set first row to 1's
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                c[0][i] = 0
                break
            else:
                c[0][i] = 1
        # set first col to 1's
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                c[i][0] = 0
                break
            else:
                c[i][0] = 1
        # current = upper val + left val
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    c[i][j] = 0
                else:
                    c[i][j] = c[i-1][j] + c[i][j-1]
        return c[m-1][n-1]