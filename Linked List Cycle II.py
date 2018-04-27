# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = dict()
        temp = head
        while temp:
            if temp not in d:
                d[temp] = 1
            else:
                return temp
            temp = temp.next
        return None
        