class Solution(object):
    def setZeroes(self, matrix):
        row = 0
        col = 0
        # first check first row and set row and col flags
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i==0:
                        row = 1
                    if j==0:
                        col = 1
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # if the row or col in first is set change
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j]== 0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        # change the first row
        if row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        