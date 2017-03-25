# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def getMinimumDifference(self, root):
        self.inorder(root)
        a = list()
        for i in range(len(self.l)-1):
            a.append(abs(self.l[i]-self.l[i+1]))
        return min(a)

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.l.append(root.val)
        self.inorder(root.right)