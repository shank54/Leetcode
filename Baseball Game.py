class Solution(object):
    def calPoints(self, ops):
        stk = list()
        a = 0
        b = 0
        c = 0
        sm = 0
        for i in range(len(ops)):
            if ops[i] == "C":
                a = stk.pop()
                sm -= int(a)
            elif ops[i] == "D":
                a = int(stk.pop())
                sm += 2*a
                stk.append(a)
                stk.append(2*a)
            elif ops[i] == "+":
                a = int(stk.pop())
                b = int(stk.pop())
                c = a+b
                sm += c
                stk.append(b)
                stk.append(a)
                stk.append(c)
            else:
                stk.append(int(ops[i]))
                sm += int(ops[i])
        return sm