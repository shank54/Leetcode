class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j>i:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        a = 0
        b = len(matrix)-1
        while a<b:
            for i in range(len(matrix)):
                matrix[i][a],matrix[i][b] = matrix[i][b],matrix[i][a] 
            a += 1
            b -= 1