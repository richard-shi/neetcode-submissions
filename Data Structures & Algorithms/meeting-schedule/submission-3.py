"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def overlaps(a, b):
    max_start = max(a.start, b.start)
    min_end = min(a.end, b.end)
    return (min_end - max_start) > 0

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        
        for i in range(1, len(intervals)):
            if overlaps(intervals[i-1], intervals[i]):
                return False

        return True


