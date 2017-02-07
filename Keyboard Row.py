class Solution(object):
    def findWords(self, words):
        a = "qwertyuiopQWERTYUIOP"
        b = "asdfghjklASDFGHJKL"
        c = "zxcvbnmZXCVBNM"
        l = list()
        for i in words:
            x = 0
            y = 0
            z = 0
            for j in i:
                if j in a:
                    x += 1
                if j in b:
                    y += 1
                if j in c:
                    z += 1
            if x>=1 and y==0 and z==0:
                l.append(i)
            elif y>=1 and x==0 and z==0:
                l.append(i)
            elif z>=1 and x==0 and y==0:
                l.append(i)
        return l