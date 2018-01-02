class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        s = ""
        for i in licensePlate:
            if i.isalpha():
                s += i.lower()
        d = dict()
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        l = []
        for word in words:
            d1 = dict()
            for i in word:
                d1.setdefault(i,0)
                d1[i] += 1
            f = 0
            for i in d:
                if i not in d1 or d[i] > d1[i]:
                    f = 1
                    break
            if f!=1:
                l.append(word)
        minlen = float('inf')
        for i in l:
            if len(i)<minlen:
                minlen = len(i)
        for i in l:
            if len(i) == minlen:
                return i
            
        