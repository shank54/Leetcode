# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def binaryTreePaths(self, root):
        s = ""
        if root==None:
            return []
        self.links(root,s)
        
        return self.l
        
    def links(self,root,s):
        if root==None:
            return
        s += str(root.val)+"->"
        if root.left==None and root.right==None:
            s=s[:-2]
            self.l.append(s)
            return
        if root.left==None:
            self.links(root.right,s)
            return
        if root.right==None:
            self.links(root.left,s)
            return
        
        self.links(root.left,s)
        self.links(root.right,s)
        
            
        