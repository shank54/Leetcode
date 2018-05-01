class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        tmp = [0]*26
        for i in range(len(S)):
            tmp[ord(S[i])-ord('a')] = i
        j = 0
        k = 0
        res = []
        for i in range(len(S)):
            j = max(j,tmp[ord(S[i])-ord('a')])
            if i == j:
                res.append(i-k+1)
                k = i+1
        return res