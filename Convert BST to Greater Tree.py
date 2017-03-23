# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
        self.m = list()
    def convertBST(self, root):
        self.inorder(root)
        n = len(self.l)
        m = len(self.l)-1
        
        while m>0 and n>0:
            n -= 1
            m -= 1
            self.l[m].val += self.l[n].val
            
        return root
        
        
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.l.append(root)
        self.inorder(root.right)

    