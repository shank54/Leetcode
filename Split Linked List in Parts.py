# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        # 1st find the length of list
        l = self.lengthOfList(root)
        while l>0 and k>0:
            # then divide the length by k and store as var d
            d = math.ceil(l/float(k))
            # move d steps and decrement d from l
            l = l-d
            tmp = root
            p = root
            tprev = None
            while d>0 and tmp:
                tprev = tmp
                tmp = tmp.next
                d -= 1
            tprev.next = None
            #tmpnxt = tmp.next
            root = tmp
            #tmp.next = None
            res.append(p)
            k -= 1
            # repeat above steps until node is null or l is 0
        while k>0:
            res.append([])
            k -= 1
        return res
    
    def lengthOfList(self,r):
        l = 0
        while r:
            r = r.next
            l += 1
        return l
        