class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A or not B or len(A)!=len(B):
            return False
        
        t = []
        # find A[0] index value in B
        for i in range(len(B)):
            if B[i] == A[0]:
                t.append(i)
        j = 0
        if len(t)==0:
            return False
        tmp = t[j]
        # Start comparing the values
        i = 0
        while i<len(A):
            if A[i] != B[tmp]:
                j += 1
                if j>=len(t):
                    return False
                tmp = t[j]
                i = 0
            tmp += 1
            if tmp >= len(B):
                tmp = 0
            i += 1
        return True