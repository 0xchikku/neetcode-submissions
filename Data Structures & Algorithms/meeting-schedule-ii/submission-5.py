"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # time - O(n logn), space - O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        end = 0
        active = 0
        start = 0
        maxRoom = 0
        while start < len(starts):
            if starts[start] < ends[end]:
                active += 1
                start += 1
            else:
                active -= 1
                end += 1
            maxRoom = max(maxRoom, active)
        return maxRoom