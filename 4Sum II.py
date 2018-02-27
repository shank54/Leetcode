class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = dict()
        
        for i in range(len(A)):
            for j in range(len(B)):
                d.setdefault(A[i]+B[j],0)
                d[A[i]+B[j]] += 1
        
        c = 0
        for i in range(len(C)):
            for j in range(len(D)):
                if -C[i]-D[j] in d:
                    c += d[-C[i]-D[j]]
        
        return c