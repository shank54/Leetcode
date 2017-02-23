class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return str(0)
        if num<0:
            a = self.conv(abs(num),7)
            return "-"+a[::-1]
        else:
            a = self.conv(abs(num),7)
            return a[::-1]
        
    def conv(self,n,m):
        if n==0:
            return 0
        d = ""
        while n:
            d+=str((n%m))
            n /= m
        return d
        