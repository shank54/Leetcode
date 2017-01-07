class Solution(object):
    def isPowerOfFour(self, num):
        if num>1:
            while num%4==0:
                num/=4
        return num==1
        