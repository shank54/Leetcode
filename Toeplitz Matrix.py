class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])):
                if j+1<len(matrix[i]) and i+1<len(matrix) and matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True