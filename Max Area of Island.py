class Solution(object):
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        mx = 0
        a = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    a = self.dfs(grid,i,j)
                    mx = max(mx,a)
        return mx
    
    def dfs(self,grid, r, c):
        rl = len(grid)
        cl = len(grid[0])
        
        if r<0 or r>=rl or c<0 or c>=cl or grid[r][c] == 0:
            return 0       
        
        grid[r][c] = 0
        return 1+ self.dfs(grid,r-1,c) + self.dfs(grid,r+1,c) + self.dfs(grid,r,c-1) + self.dfs(grid,r,c+1)
        