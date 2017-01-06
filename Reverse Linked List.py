# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        temp = head
        prev = None
        tnext = None
        while temp!=None:
            tnext = temp.next
            temp.next = prev
            prev = temp
            temp = tnext
        head = prev
        return head
            
        