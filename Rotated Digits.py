class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {"0":"0","1":"1","2":"5","6":"9","8":"8","5":"2","9":"6"}
        count = 0
        for i in range(1,N+1):
            s = str(i)
            tmp = ""
            for c in range(len(s)):
                if s[c] not in d:
                    tmp = ""
                    break
                else:
                    tmp += d[s[c]]
            if tmp and int(tmp) != int(s):
                count += 1
        return count