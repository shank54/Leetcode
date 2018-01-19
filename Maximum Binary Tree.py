# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums)<1:
            return
        m = max(nums)
        mi = nums.index(m)
        ls = 0
        le = mi-1
        rs = mi+1
        re = len(nums)-1
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[ls:le+1])
        root.right = self.constructMaximumBinaryTree(nums[rs:re+1])
        return root
        