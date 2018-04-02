# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            val = preorder.pop(0)
            i = 0
            for i in range(len(inorder)):
                if inorder[i] == val:
                    break
            indx = i
            root = TreeNode(val)
            root.left = self.buildTree(preorder,inorder[:i])
            root.right = self.buildTree(preorder,inorder[i+1:])
            return root