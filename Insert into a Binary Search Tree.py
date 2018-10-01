# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        prev = root
        temp = root
        while temp:
            if temp.val<val:
                prev = temp
                temp = temp.right
            else:
                prev = temp
                temp = temp.left
        if prev.val<val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root