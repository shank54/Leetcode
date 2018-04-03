# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            val = postorder.pop()
            i = 0
            for i in range(len(inorder)):
                if inorder[i] == val:
                    break
            indx = i
            root = TreeNode(val)
            root.right = self.buildTree(inorder[i+1:],postorder)
            root.left = self.buildTree(inorder[:i],postorder)            
            return root
        