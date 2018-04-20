# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or root == p or root ==q:
            return root
        left_k = self.lowestCommonAncestor(root.left,p,q)
        right_k = self.lowestCommonAncestor(root.right,p,q)
        if left_k and right_k:
            return root
        if left_k!=None:
            return left_k
        else:
            return right_k