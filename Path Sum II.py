# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = list()
    def pathSum(self, root, t):
        a = list()
        if root==None:
            return []
        self.paths(root)
    
        for st in self.l :
            lis = map(int,st.split())
            total=sum(lis)
            if total == t:
                a.append(lis)
        return a
        
    def paths(self,root,c_list=''):
        if root==None:
            return 
        c_list+=str(root.val)+" "
        if root.left==None and root.right==None:
            c_list=c_list[:-1]
            self.l.append(c_list)
            return
        if root.left==None:
            self.paths(root.right,c_list)
            return
        if root.right==None:
            self.paths(root.left,c_list)
            return
        
        self.paths(root.left,c_list)
        self.paths(root.right,c_list)
        