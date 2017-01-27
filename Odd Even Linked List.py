# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return head
        t1 = head
        t2=  t1.next
        p = t2
        while t1.next!=None and t2.next!=None:
            n1 = t2.next.next
            n2 = t2.next
            t1.next = n2
            t1 = n2
            t2.next = n1
            t2 = n1
        t1.next = p
        return head