class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-","").upper()
        if len(S)==0:
            return S
        l = list(S)
        i = len(l)
        j = 0
        while i>0:
            j += 1
            if j==K:
                j = 0
                l.insert(i-1,"-")
            i -= 1
        if l[0]=="-":
            del l[0]
        S = "".join(l)
        return S