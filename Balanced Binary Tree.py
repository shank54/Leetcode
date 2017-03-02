# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if root==None:
            return True
        l = self.height(root.left)
        r = self.height(root.right)
        return abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self,root):
        if root==None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
        