# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = dict()
        d[None] = None
        temp = head
        while temp:
            d[temp] = RandomListNode(temp.label)
            temp = temp.next
        temp = head
        while temp:
            d[temp].next = d[temp.next]
            d[temp].random = d[temp.random]
            temp = temp.next
        return d[head]