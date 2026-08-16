"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_end = intervals[i-1].end
            st, end = intervals[i].start, intervals[i].end

            if st < prev_end:
                return False
        
        return True