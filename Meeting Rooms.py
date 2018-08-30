# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        maxtillnow = intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start<maxtillnow:
                return False
            if intervals[i].end>maxtillnow:
                maxtillnow = intervals[i].end
        return True