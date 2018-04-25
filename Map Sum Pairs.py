class Node:
    def __init__(self):
        self.d = dict()
        self.d2 = dict()
        self.v = 0
        self.isEnd = False
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        start = self.root
        if key not in start.d2:
            start.d2[key] = 1
            for i in key:
                if i not in start.d:
                    start.d[i] = Node()
                start = start.d[i]
                start.v += val
            start.isEnd = True
        else:
            for i in key:
                if i not in start.d:
                    start.d[i] = Node()
                start = start.d[i]
                start.v = val
            start.isEnd = True
            
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        start = self.root
        for i in prefix:
            if i not in start.d:
                return 0
            start = start.d[i]
        return start.v
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)