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
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        const sortedIntervals = [...intervals].sort((interval1, interval2) => interval1.start - interval2.start)
        for (let i = 1; i < sortedIntervals.length; i++) {
            if (sortedIntervals[i-1].end > sortedIntervals[i].start) return false
        }
        return true
    }
}
