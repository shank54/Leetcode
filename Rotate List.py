# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        t = head
        l = 0
        if head==None:
            return head
        while t.next!=None:
            l += 1
            t = t.next
        t = head
        if k>l+1:
            k = k%(l+1)
        if k==l+1 or k==0:
            return head
        k = l-k
        p = None
        while t.next!=None and k>-1:
            p = t
            t = t.next
            k -= 1
        p.next = None
        #t = self.revList(t)
        p = t
        
        while p.next!=None:
            p = p.next
        p.next = head
        return t
        