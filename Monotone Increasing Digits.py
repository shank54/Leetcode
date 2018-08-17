class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = str(N)
        res = list(res)
        i = 0
        while i<len(res)-1:
            if res[i]<=res[i+1]:
                i += 1
            else:
                break
        if i==len(res)-1:
            return N
        while i>0:
            if res[i] == res[i-1]:
                i -= 1
            else:
                break
        res[i] = str(int(res[i])-1)
        i += 1
        while i<len(res):
            res[i] = "9"
            i += 1
        res = "".join(res)
        return int(res)