class Solution(object):
    def frequencySort(self, s):
        d = dict()
        for i in s:
            d.setdefault(i,0)
            d[i] += 1
        a = ""
        for i in sorted(d,key=d.get,reverse=True):
            a += d[i]*i
        return a
        