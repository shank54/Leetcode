class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split() 
        d1 = dict()
        for i in A:
            d1.setdefault(i,0)
            d1[i] += 1
        for i in B:
            d1.setdefault(i,0)
            d1[i] += 1
        res = []
        for i in d1:
            if d1[i] == 1:
                res.append(i)
        return res