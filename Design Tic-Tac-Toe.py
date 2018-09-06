class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag = 0
        self.antidiag = 0
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        length = self.n
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.diag += 1
            if row == length-1-col:
                self.antidiag += 1
            if self.rows[row] == length or self.cols[col] == length or self.diag == length or self.antidiag == length:
                return 1
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col:
                self.diag -= 1
            if row == length-1-col:
                self.antidiag -= 1
            if self.rows[row] == -length or self.cols[col] == -length or self.diag == -length or self.antidiag == -length:
                return 2
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)