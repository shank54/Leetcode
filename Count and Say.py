class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = "1"
        if n == 1:
            return start
        for i in range(2,n+1):
            tmp = ""
            j = 0
            k = 0
            flag = 1
            while j<len(start) and k<len(start):
                if start[j] == start[k]:
                    flag = 1
                    k += 1
                else:
                    flag = 0
                    tmp += str(k-j)+str(start[j])
                    j = k
            if flag:
                tmp += str(k-j)+str(start[j])
            start = tmp
        return tmp