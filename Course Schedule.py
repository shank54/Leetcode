class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = dict()
        for i in prerequisites:
            a,b = i
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
        
        vis = [0]*numCourses
        stk = [0]*numCourses
        for i in graph:
            if self.cycle(i,graph,vis,stk):
                return False
        return True
        
    def cycle(self,v,graph,vis,stk):
        vis[v] = 1
        stk[v] = 1
        if v in graph:
            for i in graph[v]:
                if vis[i] == 0:
                    if self.cycle(i,graph,vis,stk):
                        return True
                elif stk[i]:
                    return True
        stk[v] = 0
        return False