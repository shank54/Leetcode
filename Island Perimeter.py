class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        around = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 1
                    if i>=1 and grid[i-1][j]==1:
                        around += 1
                    if j>=1 and grid[i][j-1] == 1:
                        around += 1
                    if i+1<len(grid) and grid[i+1][j] == 1:
                        around += 1
                    if j+1<len(grid[0]) and grid[i][j+1] == 1:
                        around += 1
        return count*4 - around