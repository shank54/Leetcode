class Solution(object):
    def isPowerOfTwo(self, n):
        if n>0:
            if n&(n-1)==0:
                return True
            else:
                return False
        return False
                
            
        