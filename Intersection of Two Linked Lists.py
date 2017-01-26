# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lA = self.len(headA)
        lB = self.len(headB)
        while lA>lB:
            headA = headA.next
            lA -= 1
        while lB>lA:
            headB = headB.next
            lB -= 1
        while headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA
    
    def len(self,head):
        l = 0
        while head!=None:
            head = head.next
            l += 1
        return l