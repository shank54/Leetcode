class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {"6":"9","9":"6","1":"1","8":"8","0":"0"}
        res = ""
        for i in range(len(num)-1,-1,-1):
            tmp = num[i]
            if tmp in d:
                res += d[tmp]
            else:
                return False
        return res==num