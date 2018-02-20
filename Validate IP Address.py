class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
        l = []
        s = ""
        for i in IP:
            if i=="."or i==":":
                l.append(s)
                s = ""
            else:
                s += i
        l.append(s)
        if len(l)==4:
            for i in l:
                if not i.isdigit() or len(str(i))!=len(str(int(i))) or int(i)<0 or int(i)>255 :
                    return "Neither"
            return "IPv4"
        if len(l)==8:
            for i in l:
                if len(str(i))>4 or len(str(i))<=0 or not is_hex(i):
                    return  "Neither"                    
            return "IPv6"
        else:
            return "Neither"