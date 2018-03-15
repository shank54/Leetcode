# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #rt ,lf , rt
        if not root:
            return []
        stk = []
        stk.append(root)
        res = []
        while len(stk)>0:
            tmp = stk.pop()
            res.append(tmp.val)
            if tmp.right:
                stk.append(tmp.right)
            if tmp.left:
                stk.append(tmp.left)
        return res
            
        