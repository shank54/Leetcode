class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        numRows -= 2
        c = 1
        while numRows >0 :
            l = []
            l.append(1)
            for i in range(len(res[c])-1):
                tmp = res[c][i]+res[c][i+1]
                l.append(tmp)
            l.append(1)
            res.append(l)
            c += 1
            numRows -= 1
        return res