class Solution:
    # time - O(n), space - O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start = 0
        end = 1
        for index in range(len(intervals)):
            if intervals[index][end] < newInterval[start]:
                res.append(intervals[index])
            elif newInterval[end] < intervals[index][start]:
                res.append(newInterval)
                res += intervals[index:]
                return res
            else:
                newInterval[start] = min(intervals[index][start], newInterval[start])
                newInterval[end] = max(intervals[index][end], newInterval[end])
        
        res.append(newInterval)
        return res
        

