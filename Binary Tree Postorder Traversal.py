# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #lf, rt, r
        if not root:
            return []
        stk = []
        res = []
        stk.append(root)
        while len(stk)>0:
            tmp = stk.pop()
            res.append(tmp.val)
            if tmp.left:
                stk.append(tmp.left)
            if tmp.right:
                stk.append(tmp.right)
        return res[::-1]
        