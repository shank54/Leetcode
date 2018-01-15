# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l = []
        
    def inorderTraversal(self, root):
        if root == None:
            return []
        s = []
        temp = root
        flag = 0
        
        while(flag==0):
            if temp:
                s.append(temp)
                temp = temp.left
            else:
                if len(s)>0:
                    temp = s.pop()
                    self.l.append(temp.val)
                    temp = temp.right
                else:
                    flag = 1
                    
        return self.l
            
                
        