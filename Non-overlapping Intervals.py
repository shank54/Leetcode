# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x:x.end)      
        if len(intervals)<=1:
            return 0
        stk = []
        stk.append(intervals[0].start)
        stk.append(intervals[0].end)
        c = 0
        for i in range(1,len(intervals)):
            t = stk.pop()
            if intervals[i].start<t:
                c += 1
                stk.append(t)
            else:
                stk.append(t)
                stk.append(intervals[i].start)
                stk.append(intervals[i].end)
        return c
        