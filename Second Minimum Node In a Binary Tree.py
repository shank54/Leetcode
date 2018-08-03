# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.inorder(root)
        res = float('inf')
        for i in range(len(self.l)):
            if self.l[i] > root.val:
                res = min(res,self.l[i])
        if res==float('inf'):
            return -1
        return res
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)