# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.samePath(root)
        return self.res
        
    def samePath(self,root):
        if not root:
            return 0
        leftCount = self.samePath(root.left)
        rightCount = self.samePath(root.right)
        leftmax = 0
        rightmax = 0
        
        if root.left and root.left.val == root.val:
            leftmax += leftCount + 1
        if root.right and root.right.val == root.val:
            rightmax += rightCount + 1
        
        self.res = max(self.res,leftmax+rightmax)
        return max(leftmax,rightmax)
       