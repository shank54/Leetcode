class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = [0]*(n)
        for i in range(n):
            a[i] = i+1
        res = []
        for k in range((n/2)):
            i = 0
            j = len(a)-1
            while i<j:
                tmp = [a[i],a[j]]
                if i==0:
                    res = []
                res.append(tmp)
                i += 1
                j -= 1
            a = res
        b = str(a)
        b = b.replace("[","(")
        b = b.replace("]",")")
        b = b.replace(" ","")
        return b[1:-1]