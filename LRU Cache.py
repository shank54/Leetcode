class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = dict()
        self.stk = []
        self.length = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            ans = self.d[key]
            self.stk.remove(key)
            self.stk.append(key)
            return ans
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.d:
            if len(self.d)==self.length:
                temp = self.stk.pop(0)
                del self.d[temp]
            self.d[key] = value
            self.stk.append(key)
        else:
            self.d[key] = value
            self.stk.remove(key)
            self.stk.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)