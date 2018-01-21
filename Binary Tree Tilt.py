# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0
    def findTilt(self, root):
        self.diff(root)
        return self.ans
    def diff(self,root):
        if root == None:
            return 0
        lsum = self.diff(root.left)
        rsum = self.diff(root.right)
        #print lsum,rsum
        self.ans += abs(lsum-rsum)
        return lsum+rsum+root.val