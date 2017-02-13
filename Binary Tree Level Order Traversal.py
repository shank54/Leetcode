# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = dict()
    def levelOrder(self, root):
        if root==None:
            return []
        self.Level(root,0)
        l = list()
        for i in self.d:
            l.append(self.d[i])
        return l
    def Level(self,root,i):
        if root==None:
            return
        self.d.setdefault(i,[])
        self.d[i].append(root.val)
        self.Level(root.left,i+1)
        self.Level(root.right,i+1)