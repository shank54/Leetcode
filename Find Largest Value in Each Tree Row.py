# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = dict()
    def largestValues(self, root):
        l = list()
        if root==None:
            return []
        self.level(root,0)
        for i in self.d:
            l.append(max(self.d[i]))
        return l
    
    def level(self,root,i):
        if root==None:
            return
        self.d.setdefault(i,[])
        self.d[i].append(root.val)
        self.level(root.left,i+1)
        self.level(root.right,i+1)