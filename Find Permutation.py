class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [1]*(len(s)+1)
        i = 1
        j = 0
        flag = 1
        while i<=len(s):
            res[i] = i+1
            j = i
            if s[i-1] == "D":
                while i<=len(s) and s[i-1] == "D":
                    i += 1
                tmp = j-1
                for k in range(i,j-1,-1):
                    res[tmp] = k
                    tmp += 1
            else:
                i += 1
        return res