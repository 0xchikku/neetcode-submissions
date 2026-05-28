class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    // time - O(n logn), space - O(1)
    eraseOverlapIntervals(intervals) {
        const start = 0;
        const end = 1;
        intervals.sort((interval1, interval2) => interval1[end] - interval2[end]);
        let removed = 0
        let prevEnd = intervals[0][end]
        for (let i = 1; i < intervals.length; i++) {
            if (intervals[i][start] < prevEnd) {
                removed++
            } else {
                prevEnd = intervals[i][end]
            }
        }
        return removed
    }
}
