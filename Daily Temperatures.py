class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = []
        stk = []
        count = 0
        result.append(count)
        i = len(temperatures)-1
        stk.append(i)
        i -= 1
        while i>=0:
            count = 0
            while len(stk)>0 and temperatures[stk[-1]]<= temperatures[i]:
                stk.pop()
            if len(stk) == 0:
                result.append(0)
            else:
                result.append(stk[-1]-i)
            stk.append(i)
            i -= 1
        return result[::-1]