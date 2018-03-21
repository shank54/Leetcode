class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        a = 0
        mx = 0
        tmp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                a = self.dfs(matrix,i,j,float('inf'),tmp)
                mx = max(mx,a)
        
        return mx
                
    
    def dfs(self,arr,r,c,prev,tmp):
        rl = len(arr)
        cl = len(arr[0])
        if r<0 or c<0 or r>=rl or c>=cl or arr[r][c]>=prev:
            return 0
        if tmp[r][c]>0:
            return tmp[r][c]
        prev = arr[r][c]
        
        a = max(1+self.dfs(arr,r,c+1,prev,tmp),1+self.dfs(arr,r,c-1,prev,tmp),1+self.dfs(arr,r+1,c,prev,tmp),1+self.dfs(arr,r-1,c,prev,tmp))
        tmp[r][c] = a
        return a