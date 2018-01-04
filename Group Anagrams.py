class Solution(object):
    def groupAnagrams(self, strs):
        d = dict()
        for i in strs:
            a = "".join(sorted(i))
            a = str(a)
            if str(a) not in d:
                d.setdefault(a,[])
                d[a].append(i)
            else:
                d[a].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res