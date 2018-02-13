class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        opr = ["+","-","*","/"]
        for i in tokens:
            if i not in opr:
                stk.append(int(i))
            else:
                if i=="+":
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a+b)
                if i=="-":
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b-a)
                if i=="*":
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a*b)
                if i=="/":
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(int((float(b)/a)))
        return stk[0]