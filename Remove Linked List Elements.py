# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        prev = None
        temp = head
        if head==None:
            return head
        if head.next==None and head.val==val:
            return head.next
        while temp!=None and temp.next!=None:
            if temp.next.val==val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            if head.val==val:
                head = head.next
        return head
                
        