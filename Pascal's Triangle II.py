class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [[1],[1,1]]
        rowIndex -= 2
        c = 1
        while c<=rowIndex+1 :
            l = []
            l.append(1)
            for i in range(len(res[c])-1):
                tmp = res[c][i]+res[c][i+1]
                l.append(tmp)
            l.append(1)
            res.append(l)
            c += 1
        return res[c]
        