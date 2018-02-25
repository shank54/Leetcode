# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorder(root)
        for i in range(1,len(self.l)):
            if self.l[i]<=self.l[i-1]:
                return False
        return True
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)