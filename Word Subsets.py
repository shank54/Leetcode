class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        temp = ""
        dt = [0]*26
        for i in B:
            d = [0]*26
            for j in i:
                d[ord(j)-ord('a')] += 1
            for k in range(26):
                dt[k] = max(dt[k],d[k])
        
        res = []
        for word in A:
            t = [0]*26
            for j in word:
                t[ord(j)-ord('a')] += 1
            flag = 0
            for i in range(26):
                if t[i]<dt[i]:
                    flag = 1
                    break
            if flag == 0:
                res.append(word)
        return res