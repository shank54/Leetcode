class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        print str
        ans = ""
        i = 1
        flag = 0
        if str[0] == "-":
            ans += str[0]
        elif str[0].isdigit():
            ans += str[0]
        elif str[0] == "+":
            ans += ""
        else:
            return 0
        while i<len(str)-1:
            if str[i-1]=="" and str[i] == "-" and str[i+1].isdigit():
                ans += str[i]
                i += 1
            elif str[i].isdigit():
                ans += str[i]
                i += 1
            else:
                flag = 1
                break
        if flag != 1 and i<len(str):
            if str[i].isdigit():
                ans += str[i]
        if ans == "" or ans == "-":
            return 0
        if int(ans)<-2**31:
            return -2**31
        if int(ans)>(2**31)-1:
            return (2**31)-1
        return int(ans)