# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = dict()
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.subTreeSum(root)
        res = []
        m = max(self.d.values())
        for i in self.d:
            if self.d[i] == m:
                res.append(i)
        return res
    
    def subTreeSum(self,root):
        if not root:
            return 0
        s = root.val
        s += self.subTreeSum(root.left)
        s += self.subTreeSum(root.right)
        if s not in self.d:
            self.d[s] = 1
        else:
            self.d[s] += 1
        return s