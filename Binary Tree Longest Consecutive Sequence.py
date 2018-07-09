# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stk = []
        count = 1
        stk.append((root,count))
        res = 0
        c = 0
        while stk:
            tmp,count = stk.pop()
            if tmp.left:
                if tmp.left.val == tmp.val+1:
                    c = count + 1
                else:
                    c = 1
                stk.append((tmp.left,c))
            if tmp.right:
                if tmp.right.val == tmp.val+1:
                    c = count + 1
                else:
                    c = 1
                stk.append((tmp.right,c))
            res = max(res,count)
        return res