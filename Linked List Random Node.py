from random import randint

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        temp = self.head
        c = 0
        while temp.next:
            c += 1
            temp = temp.next
        r = randint(1,c+1)
        t = 1
        temp = self.head
        while t<r and temp:
            t += 1
            temp = temp.next
        return temp.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()