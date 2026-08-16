"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = [], []
        n = len(intervals)

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        rooms = 0
        curr_active = 0
        s, e = 0, 0

        while s < n and e < n:
            if starts[s] < ends[e]:
                curr_active += 1
                rooms = max(rooms, curr_active)
                s += 1
            else:
                e += 1
                curr_active -= 1
        
        return rooms