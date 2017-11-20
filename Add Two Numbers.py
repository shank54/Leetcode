# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        n1 = self.listlen(l1)
        n2 = self.listlen(l2)
        nt1 = ListNode(0)
        nt2 = ListNode(0)
        s = 0 
        a = 0
        b = 0
        f = 0
        if n1>=n2:
            while t1:
                if t2 == None:
                    b = 0
                else:
                    b = t2.val
                    t2 = t2.next
                s = t1.val+b+f
                f = 0
                if s>9:
                    a = s%10
                    s = s/10
                    f = s
                    s = a
                t1.val = s
                t1 = t1.next
            t1 = l1
            while t1.next:
                t1 = t1.next
            if f>0:
                nt1.val = f
                t1.next = nt1
            return l1
        else:
            while t2:
                if t1 == None:
                    b = 0
                else:
                    b = t1.val
                    t1 = t1.next
                s = t2.val+b+f
                f = 0
                if s>9:
                    a = s%10
                    s = s/10
                    f = s
                    s = a
                t2.val = s
                t2 = t2.next
            t2= l2
            while t2.next:
                t2 = t2.next
            if f>0:
                nt2.val = f
                t2.next = nt2
            return l2
                
        
    def listlen(self,l):
        t = l
        c = 0
        while t:
            t = t.next
            c += 1
        return c
        