class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = 0
                if grid[i][j] == "0":
                    if i-1>=0:
                        k = i-1
                        while k >=0:
                            if grid[k][j] == "W":
                                break
                            elif grid[k][j] == "0":
                                k -= 1
                            elif grid[k][j] == "E":
                                count += 1
                                k -= 1
                        
                    if i+1<len(grid):
                        k = i+1
                        while k < len(grid):
                            if grid[k][j] == "W":
                                break
                            elif grid[k][j] == "0":
                                k += 1
                            elif grid[k][j] == "E":
                                count += 1
                                k += 1
                        
                    if j-1 >=0:
                        k = j-1
                        while k >=0:
                            if grid[i][k] == "W":
                                break
                            elif grid[i][k] == "0":
                                k -= 1
                            elif grid[i][k] == "E":
                                count += 1
                                k -= 1
                        
                    if j+1 < len(grid[i]):
                        k = j+1
                        while k < len(grid[i]):
                            if grid[i][k] == "W":
                                break
                            elif grid[i][k] == "0":
                                k += 1
                            elif grid[i][k] == "E":
                                count += 1
                                k += 1
                res = max(res,count)
        return res
                        