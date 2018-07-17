class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for string in strings:
            tmp = []
            for k in range(1,len(string)):
                tmp.append(str((ord(string[k])-ord(string[k-1]))%26))
            hs = "".join(tmp)
            if hs not in d:
                d[hs] = [string]
            else:
                d[hs].append(string)
        res = []
        for i in d:
            res.append(d[i])
        
        return res