# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        
        if root==None :
            return True
        r2=self.mirror(root.right)
        
        return self.isSame(root.left,r2)
    
    def isSame(self,root1,root2) :
        if root1==None and root2==None :
            return True
        
        if root1==None or root2==None :
            return False

        if root1.val!=root2.val :
            return False
        
        return self.isSame(root1.left,root2.left) and self.isSame(root1.right,root2.right)    
    

    def mirror(self,root):
        if root==None:
            return None
        
        left=root.left
        right=root.right
        
        root.left=right
        root.right=left
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root
            
        