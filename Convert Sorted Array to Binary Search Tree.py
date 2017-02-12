# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        
        if len(nums)==1 :
            return TreeNode(nums[0])
        
        
        mid = len(nums)/2
        print nums[mid]
        t = TreeNode(nums[mid])
        t.left = self.sortedArrayToBST(nums[:mid])
        t.right = self.sortedArrayToBST(nums[mid+1:])
        return t