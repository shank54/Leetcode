import re
class Solution(object):
    def wordPattern(self, pattern, str):
        d1 = dict()
        d2 = dict()
        s = str.split(" ")
        c = 0
        e = 0
        for i in range(len(pattern)):
            if pattern[i] not in d1:
                c = 1
                d1[pattern[i]] = c
            else:
                c += 1
                d1[pattern[i]] = c
        for i in range(len(s)):
            if s[i] not in d2:
                e = 1
                d2[s[i]] = e
            else:
                e += 1
                d2[s[i]] = e
        l1 = list()
        l2 = list()
        for i in pattern :
           l1.append(d1[i])
        for i in s :
           l2.append(d2[i])        
        return l1==l2
        