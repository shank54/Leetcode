class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if self.inc(A):
            return True
        elif self.dec(A):
            return True
        elif self.same(A):
            return True
        return False
    
    def inc(self,A):
        for i in range(1,len(A)):
            if A[i]-A[i-1]<0:
                return False
        return True
    
    def dec(self,A):
        for i in range(1,len(A)):
            if A[i]-A[i-1]>0:
                return False
        return True
    
    def same(self,A):
        for i in range(1,len(A)):
            if A[i]-A[i-1] != 0:
                return False
        return True