class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        vis = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word,0,vis):
                    return True
        return False
    
    def dfs(self,board,row,col,word,index,vis):
        if len(word) == index:
            return True
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or vis[row][col] == 1 or word[index] != board[row][col]:
            return False
        vis[row][col] = 1
        if self.dfs(board,row-1,col,word,index+1,vis) or self.dfs(board,row+1,col,word,index+1,vis) or self.dfs(board,row,col-1,word,index+1,vis) or self.dfs(board,row,col+1,word,index+1,vis):
            return True
        vis[row][col] = 0
        return False