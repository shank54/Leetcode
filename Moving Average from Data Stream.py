class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.arr = []
        self.size = size
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.arr.append(val)
        if len(self.arr)<= self.size:
            return self.sum/float(len(self.arr))
        else:
            self.sum -= self.arr[len(self.arr)-1-self.size]
            return self.sum/float(self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)