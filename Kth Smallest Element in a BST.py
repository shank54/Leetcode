# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def kthSmallest(self, root, k):
        self.k = k
        self.trav(root)
        return self.l[k-1]
        
    def trav(self,root):
        if root != None and len(self.l)<self.k:
            self.trav(root.left)
            self.l+=[root.val]
            self.trav(root.right)
        
        
        