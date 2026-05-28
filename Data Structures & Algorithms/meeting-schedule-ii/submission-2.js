/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    // time - O(n logn), space - O(n)
    minMeetingRooms(intervals) {
        const startTime = []
        const endTime = []
        for (const interval of intervals) {
            startTime.push(interval.start);
            endTime.push(interval.end);
        }
        startTime.sort((a,b) => a-b);
        endTime.sort((a,b) => a-b);
        let active = 0
        let start = 0
        let end = 0
        let maxRoom = 0
        while (start < startTime.length) {
            if (startTime[start] < endTime[end]) {
                active += 1
                start++
                maxRoom = Math.max(maxRoom, active)
            } else {
                end++
                active -= 1
            }
        }
        return maxRoom;
    }
}
