class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = list(s)
        flag = 0
        res = []
        for i in range(1,len(l)):
            if l[i] == "+" and l[i-1] == "+":
                l[i] = "-"
                l[i-1] = "-"
                flag = 1
            if flag == 1:
                tmp = "".join(l)
                res.append(tmp)
                l[i] = "+"
                l[i-1] = "+"
                flag = 0
        return res
        