"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = dict()
        for i in employees:
            d.setdefault(i.id,i)
        return self.dfs(id,d)
        
    def dfs(self,i,d):
        res = d[i].importance
        for s in d[i].subordinates:
            res += self.dfs(s,d)
        return res