# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        # find mid
        slow = head
        fast = head
        pslow = None
        while fast and fast.next:
            pslow = slow
            slow = slow.next
            fast = fast.next.next
        # divide list start to mid-1 and mid+1 to end
        if pslow:
            pslow.next = None
        else:
            head = None
        # root is mid
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
        
        