# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(self.comp_lists)
        temp = [0]*len(intervals)
        for i in intervals:
            for j in range(len(temp)):
                if temp[j]<=i.start:
                    temp[j] = i.end
                    break
        count = 0
        for i in temp:
            if i==0:
                return count
            else:
                count += 1
        return count
    
    def comp_lists(self,first,second):
        if first.start<second.start:
            return -1
        elif first.start == second.start:
            if first.end<second.end:
                return 1
            else:
                return -1
        else:
            return 1