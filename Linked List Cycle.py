# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head==None:
            return False
        p1 = head
        p2 = head
        
        while p2.next!=None and p2.next.next!=None:
            p1 = p1.next
            p2 = p2.next.next
            
            if p1==p2:
                return True
        return False
        