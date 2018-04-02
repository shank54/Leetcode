# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorder(root)
        mini = float('inf')
        tmp = 0
        for i in range(1,len(self.l)):
            tmp = self.l[i]-self.l[i-1]
            if tmp<mini:
                mini = tmp
        return mini
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)