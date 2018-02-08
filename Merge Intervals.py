# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)        
        if len(intervals)<=1:
            return intervals
        stk = []
        stk.append(intervals[0].start)
        stk.append(intervals[0].end)
        for i in range(1,len(intervals)):
            t = stk.pop()
            if intervals[i].start<=t:
                if t<=intervals[i].end:
                    stk.append(intervals[i].end)
                else:
                    stk.append(t)
            else:
                stk.append(t)
                stk.append(intervals[i].start)
                stk.append(intervals[i].end)
        newlst = []
        while len(stk)>0:
            a = stk.pop(0)
            b = stk.pop(0)
            newlst.append([a,b])
        return newlst
