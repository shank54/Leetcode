class Solution(object):
    def repeatedSubstringPattern(self, str):
        def numbers(n):
            l = list()
            for i in range(1,n/2+1):
                if n%i==0:
                    l.append(i)
            return l
        l = len(str)
        n = numbers(l)
        for i in n:
            b = str[0:i]*(l/i)
            if b == str:
                return True
        return False