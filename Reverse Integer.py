class Solution(object):
    def reverse(self, x):
        if x>=0 and x<=9:
            return x
        if x>0:
            y = int(str(x)[::-1])
            if y>2147483647:
                return 0
            return y
        else:
            x=-x
            y=int(str(x)[::-1])
            if -y<=-2147483647:
                return 0
            return -y