class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        prev_st, prev_end = intervals[0]
        
        for i in range(1, len(intervals)):
            prev_st, prev_end = res[-1]
            s, e = intervals[i]
            if prev_end >= s:
                res.pop()
                # merge and add to res
                res.append([min(prev_st,s), max(prev_end, e)])
            else:
                res.append(intervals[i])
        
        return res



