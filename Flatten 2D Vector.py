class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.ele = 0
        self.lindex = 0

    def next(self):
        """
        :rtype: int
        """
        temp = self.vec2d[self.lindex][self.ele]
        self.ele += 1
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.lindex<len(self.vec2d):
            if self.ele<len(self.vec2d[self.lindex]):
                return True
            else:
                self.lindex += 1
                self.ele = 0
        return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())