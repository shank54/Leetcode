# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        total = len(lists)
        skips = 1
        while skips<total:
            for i in range(0,total-skips,skips*2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+skips])
            skips *= 2
        if total>0:
            return lists[0]
        return lists
        
    def mergeTwoLists(self,l1,l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val>l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1