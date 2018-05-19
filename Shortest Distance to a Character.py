class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(S)):
            if S[i] == C:
                if S[i] not in d:
                    d[C] = [i]
                else:
                    d[C].append(i)
        res = []
        for i in range(len(S)):
            if S[i]!=C:
                m = float('inf') 
                for j in range(len(d[C])):
                    m = min(m,abs(d[C][j]-i))
                res.append(m)
            else:
                res.append(0)
        return res