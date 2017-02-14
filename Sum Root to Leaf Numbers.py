# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def sumNumbers(self, root):
        
        if root==None :
            return 0
        
        self.paths(root)    
        
        total=sum(map(int,self.l))
        
        return total
        
            
        
        
    def paths(self,root,current_list=''):


        current_list+=str(root.val)

        
        if root.left==None and root.right==None :
            self.l.append(current_list)
            return
        
        if root.left==None :
            self.paths(root.right,current_list)
            return
        
        if root.right==None :
            self.paths(root.left,current_list)
            return
        
        self.paths(root.left,current_list)
        self.paths(root.right,current_list)
            
      