class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk = []
        num = 0
        res = ""
        i = 0
        while i<len(s):
            if str(s[i]).isdigit():
                tmp = ""
                while i<len(s) and str(s[i]).isdigit():
                    tmp += s[i]
                    i += 1
                num = int(tmp)
            elif s[i] == "[":
                stk.append(res)
                stk.append(num)
                num = 0
                res = ""
                i += 1
            elif s[i] == "]":
                tmpnum = stk.pop()
                tmpstr = stk.pop()
                res = tmpstr + tmpnum*res
                i += 1
            else:
                res += s[i]
                i += 1
        return res
                
        