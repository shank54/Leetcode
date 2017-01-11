class Solution(object):
    def findComplement(self, num):
        a = bin(num)[2:]
        b = ''
        for i in range(len(a)):
            if a[i]=='1':
                b+='0'
            else:
                b+='1'
        return int(b,2)