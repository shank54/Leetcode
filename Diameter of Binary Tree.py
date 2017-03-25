# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root==None:
            return 0
        else:
            lheight = self.mHeight(root.left)
            rheight = self.mHeight(root.right)
            lD = self.diameterOfBinaryTree(root.left)
            rD = self.diameterOfBinaryTree(root.right)

        return max(lheight+rheight,max(lD,rD))
        
    def mHeight(self,root):
        if root==None:
            return 0
        else:
            l = self.mHeight(root.left)
            r = self.mHeight(root.right)
        return max(l+1,r+1)
    
        