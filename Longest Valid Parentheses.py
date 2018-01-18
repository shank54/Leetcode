class Solution(object):
    def longestValidParentheses(self, s):
        stk = []
        stk.append(-1)
        c = 0
        a = ""
        l = 0
        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            else:
                stk.pop()
                if len(stk) == 0:
                    stk.append(i)
                l = max(l,i-stk[len(stk)-1])
        return l
    def ismatch(self,a,b):
        if (a=="(" and b==")"):
            return True