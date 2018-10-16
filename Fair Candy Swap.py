class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d1 = dict()
        for i in A:
            d1.setdefault(i,0)
            d1[i] += 1
        d2 = dict()
        for i in B:
            d2.setdefault(i,0)
            d2[i] += 1
        s = (sum(A)-sum(B))/2
        for i in d2:
            if s+i in d1:
                return [s+i,i]