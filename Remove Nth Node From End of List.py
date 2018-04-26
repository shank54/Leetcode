# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # fast and slow pointer and prev
        # move fast n steps until end of list
        # return slow
        temp = head
        slow = temp
        fast = temp
        prev = slow
        while fast and n>0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        if slow==head:
            return head.next
        return head
        