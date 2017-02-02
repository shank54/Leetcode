# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root==None:
            return 0
        a = 0
        st = [root]
        while st:
            node = st.pop()
            if node.left!=None:
                if node.left.left==None and node.left.right==None:
                    a += node.left.val
                else:
                    st.append(node.left)
            if node.right!=None:
                st.append(node.right)
        return a