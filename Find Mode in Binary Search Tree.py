# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def findMode(self, root):
        d = dict()
        self.trav(root)
        for i in self.l:
            d.setdefault(i,0)
            d[i] += 1
        a = list()
        m = 0
        for i in d:
            if d.get(i)>=m:
                m = d.get(i)
        for i in d:
            if d.get(i)>=m:
                a.append(i)
                m = d.get(i)
        return a
    
    def trav(self,root):
        if root==None:
            return
        self.l.append(root.val)
        self.trav(root.left)
        self.trav(root.right)