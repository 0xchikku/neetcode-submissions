class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    // time - O(n logn), space - O(n)
    merge(intervals) {
        const start = 0;
        const end = 1;
        intervals.sort((interval1, interval2) => interval1[start] - interval2[start]);
        const len = intervals.length;
        const output = [intervals[0]];
        for (let i = 1; i < len; i++) {
            const outputLen = output.length;
            if (output[outputLen-1][end] >= intervals[i][start]) {
                output[outputLen-1][end] = Math.max(output[outputLen-1][end], intervals[i][end]);
            } else {
                output.push(intervals[i]);
            }
        }
        return output;
    }
}
