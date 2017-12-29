class Solution(object):
    def complexNumberMultiply(self, a, b):
        a = a.split("+")
        b = b.split("+")
        a[1] = a[1].replace("i","")
        b[1] = b[1].replace("i","")
        img = int(a[1])+int(b[1])
        ans = int(a[0])*int(b[0])+int(a[1])*int(b[1])*-1
        bns = str(int(str(int(a[1])*int(b[0])))+int(str(int(a[0])*int(b[1]))))+"i"
        return str(ans)+"+"+str(bns)