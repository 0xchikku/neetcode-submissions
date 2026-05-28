class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {
        const output = [];
        const start = 0;
        const end = 1;
        for (let i = 0; i < intervals.length; i++) {
            if (newInterval[start] > intervals[i][end]) {
                output.push(intervals[i]);
            } else if (newInterval[end] < intervals[i][start]) {
                output.push(newInterval, ...intervals.slice(i));
                return output;
            } else {
                newInterval = [
                    Math.min(newInterval[start], intervals[i][start]),
                    Math.max(newInterval[end], intervals[i][end])
                ]
            }
        }
        output.push(newInterval);
        return output;
    }
}
