class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            board = []
            return
        
        m = len(board)
        n = len(board[0])
        c = 0
        for i in range(n):
            if board[0][i] == "O":
                    self.dfs(board,0,i,"O","Y")
        
        for i in range(m):
            if board[i][n-1] == "O":
                    self.dfs(board,i,n-1,"O","Y")
        
        for i in range(n):
            if board[m-1][i] == "O":
                    self.dfs(board,m-1,i,"O","Y")
        
        for i in range(m):
            if board[i][0] == "O":
                    self.dfs(board,i,0,"O","Y")
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(n):
            if board[0][i] == "Y":
                    self.dfs(board,0,i,"Y","O")
        
        for i in range(m):
            if board[i][n-1] == "Y":
                    self.dfs(board,i,n-1,"Y","O")
        
        for i in range(n):
            if board[m-1][i] == "Y":
                    self.dfs(board,m-1,i,"Y","O")
        
        for i in range(m):
            if board[i][0] == "Y":
                    self.dfs(board,i,0,"Y","O")
        
    def dfs(self,arr,r,c,pval,val):
        rl = len(arr)
        cl = len(arr[0])
        
        if r<0 or r>=rl or c<0 or c>=cl or arr[r][c] != pval:
            return
        arr[r][c] = val
        self.dfs(arr,r+1,c,pval,val)
        self.dfs(arr,r-1,c,pval,val)
        self.dfs(arr,r,c+1,pval,val)
        self.dfs(arr,r,c-1,pval,val)