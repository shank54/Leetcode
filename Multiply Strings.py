class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0]=="0" or num2[0]=="0":
            return "0"
        i = len(num2)-1
        p = 0
        res = 0
        x = 0
        while i>=0:
            tmp1 = ""
            j = len(num1)-1
            carry = 0
            r = ""
            sub = ""
            while j>=0:
                tmp1 = str(int(num1[j])*int(num2[i])+carry)
                carry = 0
                if len(tmp1)>1:
                    sub += tmp1[-1]
                    carry = int(tmp1[0])
                else:
                    sub += tmp1[0]
                j -= 1
            if carry!=0:
                r = str(carry)+sub[::-1]
            else:
                r = sub[::-1]
            x = int(r)*(10**p)
            res += x
            p += 1
            i -= 1
        return str(res)
    