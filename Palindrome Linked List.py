# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        a = list()
        t = head
        c = d = 0
        if head==None:
            return True
        # Iterate the list for 1st time and 
        # push the elements of list into the stack.
        # Keep track of number of elements in the list.
        while t!=None:
            a.append(t.val)
            t = t.next
            c+=1
        t = head
        # For the 2nd iteration pop the elements from the list 
        # and check with the elements in the list.
        # Increment the counter if the elements are equal.
        while t!=None:
            if t.val==a.pop():
                d+=1
            t = t.next
        # Now check if both the counters are equal.
        if c==d:
            return True
        else:
            return False