# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        temp = head
        if head==None or head.next==None:
            return
        q = temp
        prev=None
        
        while q!=None and q.next!=None:
            prev=temp
            temp = temp.next
            q = q.next.next
        
        if prev!=None :
            prev.next=None
        a = self.reverse(temp) #temp is middle node
        self.mer(head,a)
     
     # reverse 2nd half of list       
    def reverse(self, h):
        if h.next==None:
            return h
        temp = h
        prev = None
        tnext = None
        while temp!=None:
            tnext = temp.next
            temp.next = prev
            prev = temp
            temp = tnext
        h = prev
        return h
        
    # merge two lists
    def mer(self,l1,l2):
        while l1.next!=None and l2.next!=None:
            n1 = l1.next
            n2 = l2.next
            l1.next = l2
            l2.next = n1
            l1 = n1
            l2 = n2
        if l1==None and l2==None:
            return l1
        else:
            l1.next = l2
            return l1
    
        