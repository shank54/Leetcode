class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[i])):
                s = M[i][j]
                count = 1
                if i-1>=0 and j>=0:
                    s += M[i-1][j]
                    count += 1
                if i-1>=0 and j+1<len(M[i]):
                    s += M[i-1][j+1]
                    count += 1
                if i>=0 and j+1<len(M[i]):
                    s += M[i][j+1]
                    count += 1
                if i+1<len(M) and j+1<len(M[i]):
                    s += M[i+1][j+1]
                    count += 1
                if i+1<len(M) and j<len(M[i]):
                    s += M[i+1][j]
                    count += 1
                if i+1<len(M) and j-1>=0:
                    s += M[i+1][j-1]
                    count += 1
                if i>=0 and j-1>=0:
                    s += M[i][j-1]
                    count += 1
                if i-1>=0 and j-1>=0:
                    s += M[i-1][j-1]
                    count += 1
                res[i][j] = s/count
        return res
                