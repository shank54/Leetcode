class Solution(object):
    def isIsomorphic(self, s, t):
        d1 = dict()
        d2 = dict()
        c = 0
        e = 0
        for i in range(len(s)):
            if s[i] not in d1:
                c = 1
                d1[s[i]] = c
            else:
                c += 1
                d1[s[i]] = c
        for i in range(len(t)):
            if t[i] not in d2:
                e = 1
                d2[t[i]] = e
            else:
                e += 1
                d2[t[i]] = e
        l1 = list()
        l2 = list()
        for i in s :
           l1.append(d1[i])
        for i in t :
           l2.append(d2[i])        
        if l1==l2:
            return True
        else:
            return False
        