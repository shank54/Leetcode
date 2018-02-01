class Solution(object):
    def numJewelsInStones(self, J, S):
        d = dict()
        for i in J:
            d.setdefault(i,0)
            d[i] += 1
        c = 0
        for i in S:
            if i in d:
                c += 1
        return c
        