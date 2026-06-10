"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sweeping line algorithm
        mpp = defaultdict(int)
        for i in intervals:
            mpp[i.start] += 1
            mpp[i.end] -= 1
        
        prev, res = 0, 0

        for i in sorted(mpp.keys()):
            prev += mpp[i]
            res = max(res, prev)
        
        return res