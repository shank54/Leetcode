# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        return  self.hasPath(root,sum)
        
    def hasPath(self,root,total):
        if root==None:
            return (total==0)

        total-=root.val 

        if root.left==None and root.right==None:

            return (total==0)

        if root.left==None:
            return self.hasPath(root.right,total)
        if root.right==None:
            return self.hasPath(root.left,total)
            
            
        return self.hasPath(root.left,total) or self.hasPath(root.right,total)
        