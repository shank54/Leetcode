# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val>key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
        return root
    
    def findMin(self,root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp