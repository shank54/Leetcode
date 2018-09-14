class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(prerequisites)):
            if prerequisites[i][1] not in d:
                d[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                d[prerequisites[i][1]].append(prerequisites[i][0])
        for i in range(numCourses):
            if i not in d:
                d[i] = []
        checkvis = [0]*numCourses
        checkstk = [0]*numCourses
        for i in d:
            if self.cycle(i,d,checkvis,checkstk):
                return []
        vis = []
        stk = []        
        for vertex in d:
            if vertex not in vis:
                self.topSort(vertex,d,vis,stk)
        
        return stk[::-1]
    
    def cycle(self,v,d,checkvis,checkstk):
        checkvis[v] = 1
        checkstk[v] = 1
        if v in d:
            for i in d[v]:
                if checkvis[i] == 0:
                    if self.cycle(i,d,checkvis,checkstk):
                        return True
                elif checkstk[i]:
                    return True
        checkstk[v] = 0
        return False
    
    def topSort(self,vertex,d,vis,stk):
        if vertex in vis:
            stk.append(None)
            return None
        vis.append(vertex)
        if vertex in d:
            for i in d[vertex]:
                if i not in vis:
                    self.topSort(i,d,vis,stk)
            stk.append(vertex)
        else:
            stk.append(vertex)