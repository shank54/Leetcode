class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        res = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                res[i][j] = board[i][j]
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                if i-1>=0 and j-1>=0 and res[i-1][j-1] == 1:
                    count += 1
                if i-1 >=0 and j>=0 and res[i-1][j] == 1:
                    count += 1
                if i-1 >=0 and j+1<len(board[i]) and res[i-1][j+1] == 1:
                    count += 1
                if i>=0 and j+1 < len(board[i]) and res[i][j+1] == 1:
                    count += 1
                if i+1<len(board) and j+1<len(board[i]) and res[i+1][j+1] == 1:
                    count += 1
                if i+1<len(board) and j>=0 and res[i+1][j] == 1:
                    count += 1
                if i+1 < len(board) and j-1>=0 and res[i+1][j-1] == 1:
                    count += 1
                if i>=0 and j-1>=0 and res[i][j-1] == 1:
                    count += 1
                if res[i][j] == 1:
                    if count < 2:
                        board[i][j] = 0
                    elif count > 3:
                        board[i][j] = 0
                    elif count == 2 or count == 3:
                        board[i][j] = 1                    
                if res[i][j] == 0:
                    if count == 3:
                        board[i][j] = 1
                    