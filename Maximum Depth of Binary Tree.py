# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        return max(a,b) + 1
        