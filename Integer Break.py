class Solution(object):
    def integerBreak(self, n):
        a = n/3
        if n==2:
            return 1
        if n==3:
            return 2
        if n%3==0:
            return 3**a
        elif n%3==1:
            return 4*(3**(a-1))
        else:
            return 2*(3**a)
    
        