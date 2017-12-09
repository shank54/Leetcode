class Solution(object):
    def longestWord(self, words):
        l = list()
        words.sort(reverse=True)
        d = dict()
        for i in words:
            d.setdefault(i,0)
            d[i] += 1
        for i in words:
            c = 0
            for j in range(len(i)):
                if i[:len(i)-j-1] in d:
                    c += 1
            if c==len(i)-1:
                l.append(i)
        l.sort()
        m = 0
        s = ""
        for i in l:
            if len(i)>m:
                m = len(i)
                s = i
        return s