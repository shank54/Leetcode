class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        same = 1
        res = []
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                same += 1
            else:
                if same >= 3:
                    res.append([i-same,i-1])
                same = 1
        if same>=3:
            res.append([i-same+1,i])
        return res