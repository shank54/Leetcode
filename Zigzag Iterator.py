class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = []
        if v1:
            self.q.append(v1)
        if v2:
            self.q.append(v2)

    def next(self):
        """
        :rtype: int
        """
        tmp = self.q.pop(0)
        val = tmp.pop(0)
        if tmp:
            self.q.append(tmp)
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.q:
            return True
        return False
        
        


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())