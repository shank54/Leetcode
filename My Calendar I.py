class MyCalendar(object):

    def __init__(self):
        self.cal = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s,e in self.cal:
            if s<end and start<e:
                return False
        self.cal.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)