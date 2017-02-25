# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        p1 = ListNode(0)
        p2 = ListNode(0)
        a = p1
        b = p2
        t = head
        while t:
            if t.val<x:
                p1.next = t
                p1 = p1.next
            else:
                p2.next = t
                p2 = p2.next
            t = t.next
        p1.next = b.next
        p2.next = None
        return a.next