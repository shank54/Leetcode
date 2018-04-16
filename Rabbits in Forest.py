class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        s = 0
        d = dict()
        for i in answers:
            if i==0:
                s += 1
                continue
            elif i not in d:
                d[i] = 0
                s += i+1
            else:
                d[i] = d[i]+1
                if d[i] == i:
                    del d[i]
        return s