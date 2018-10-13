class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = bin(N)[2:]
        d = dict()
        for i in range(len(temp)):
            if temp[i] not in d:
                d[temp[i]] = [i]
            else:
                d[temp[i]].append(i)
        t = d['1']
        t.sort()
        ans = 0
        for i in range(1,len(t)):
            ans = max(ans,t[i]-t[i-1])
        return ans