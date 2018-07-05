class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = dict()
        for i in edges:
            a,b = i
            if a in graph:
                graph[a].append(b)
            if b in graph:
                graph[b].append(a)
            if a not in graph:
                graph[a] = [b]
            if b not in graph:
                graph[b] = [a]
        
        vis = []
        stk = []
        count = 0
        for i in range(n):
            if i not in vis:
                count += 1
                vis.append(i)
                stk.append(i)
                while stk:
                    tmp = stk.pop()
                    vis.append(tmp)
                    if tmp in graph:
                        for w in graph[tmp]:
                            if w not in vis:
                                stk.append(w)
        return count
                