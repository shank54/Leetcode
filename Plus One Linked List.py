# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        rev = self.reverse(head)
        tmp = rev
        carry = 1
        while tmp:
            prev = tmp
            if tmp.val == 9:
                if carry:
                    tmp.val = 0
                    carry = 1
            else:
                tmp.val += carry
                carry = 0
            tmp = tmp.next
        if carry:
            newNode = ListNode(carry)
            prev.next = newNode
        return self.reverse(rev)
    
    
    def reverse(self,head):
        prev = None
        tmp = head
        while tmp:
            cur = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = cur
        return prev
        