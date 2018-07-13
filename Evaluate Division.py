class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = dict()
        for i in range(len(equations)):
            a,b = equations[i]
            val = values[i]
            if (a,1) not in graph:
                graph[(a,1)] = [(a,1.0)]
            if (b,1) not in graph:
                graph[(b,1)] = [(b,1.0)]
            if (a,1) in graph:
                graph[(a,1)].append((b,val))
            if (b,1) in graph:
                if val !=0:
                    graph[(b,1)].append((a,1/float(val)))
        
        ans = []
        for i in queries:
            start,end = i
            vis = []
            stk = []
            vis.append(start)
            stk.append((start,1))
            res = 1.0
            flag = 0
            while stk:
                tmp,val = stk.pop()
                if (tmp,1) in graph:
                    if tmp == end:
                        flag = 1
                        res = val
                        break
                    for w in graph[(tmp,1)]:
                        a,b = w
                        if a not in vis:
                            res *= b
                            stk.append((a,val*b))
                            vis.append(a)
                else:
                    res = -1.0
            if flag == 0:
                res = -1.0
            ans.append(res)
        return ans
                    
            
            