# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff = float('inf')
        cur = root
        ans = root
        while cur:
            d = abs(cur.val-target)
            if d<=diff:
                diff = d
                ans = cur
            if target<cur.val:
                cur = cur.left
            elif target>cur.val:
                cur = cur.right
            else:
                break
        return ans.val