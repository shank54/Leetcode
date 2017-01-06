# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        if temp == None:
            return head
        while temp.next!=None:
            if temp.val == temp.next.val:
                p = temp.next.next
                temp.next = None
                temp.next = p
            else:
                temp = temp.next
        return head
        