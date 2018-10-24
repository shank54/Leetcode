# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp = []
        self.inorder(root,temp)
        ans = TreeNode(0)
        res = ans
        for i in temp:
            ans.right = TreeNode(i)
            ans = ans.right
        return res.right
    
    def inorder(self,root,temp):
        if root:
            self.inorder(root.left,temp)
            temp.append(root.val)
            self.inorder(root.right,temp)