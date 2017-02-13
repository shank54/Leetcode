# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root==None:
            return None
        m = root.val
        if p==None or q==None:
            return None
        if p.val<m and q.val<m:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>m and q.val>m:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        