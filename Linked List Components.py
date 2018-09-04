# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        d = dict()
        for i in G:
            if i not in d:
                d[i] = 1
        connected = 0
        temp = head
        while temp.next:
            if temp.val in d and temp.next.val not in d:
                connected += 1
            temp = temp.next
        if temp.val in d and temp.next == None:
            connected += 1
        return connected