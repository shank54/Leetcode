class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            if n==1:
                return True
            return False
        d = dict()
        for i in range(len(edges)):
            x,y = edges[i]
            if x==y:
                return False
            if x not in d:
                d[x] = [y]
            else:
                d[x].append(y)
            if y not in d:
                d[y] = [x]
            else:
                d[y].append(x)
        if len(d) != n:
            return False
        q = []
        q.append(min(d))
        vis = []
        vis.append(0)
        while q:
            temp = q.pop(0)
            for nei in d[temp]:
                if nei in q:
                    return False
                if nei not in vis:
                    q.append(nei)
                    vis.append(nei)
        for i in d:
            if i not in vis:
                return False
        return True