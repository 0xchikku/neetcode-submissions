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
    minMeetingRooms(intervals) {
        // approach is 
        // maintain start and end time array, both sorted 
        // have a start and end pointer
        // have a current active and max room counter
        // loop through start and end array
        // if start < end then active++, start++
        // else active--, end++
        // update max room
        // after loop, return max room

        const startTime = [];
        const endTime = [];
        for(const interval of intervals) {
            startTime.push(interval.start);
            endTime.push(interval.end);
        }
        startTime.sort((a,b) => a-b);
        endTime.sort((a,b) => a-b);
        let start = 0;
        let end = 0;
        let active = 0;
        let maxRoom = 0;
        while (start < startTime.length) {
            if (startTime[start] < endTime[end]) {
                active++;
                start++;
            } else {
                active--;
                end++
            }
            maxRoom = Math.max(maxRoom, active)
        }
        return maxRoom;
    }
}
