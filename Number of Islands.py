class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    c += 1
                    self.dfs(grid,i,j)
        return c
    
    def dfs(self,grid, r, c):
        rl = len(grid)
        cl = len(grid[0])
        
        if r<0 or r>=rl or c<0 or c>=cl or grid[r][c] == "0":
            return
        
        grid[r][c] = "0"
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
        