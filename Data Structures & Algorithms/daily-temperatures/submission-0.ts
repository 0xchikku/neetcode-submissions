class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    // Time - O(n), Space - O(n)
    dailyTemperatures(temperatures: number[]): number[] {
        const len = temperatures.length
        const res = Array(len).fill(0)
        const trackWaitingIndex = []
        for (let curIndex = 0; curIndex < len; curIndex++) {
            while (trackWaitingIndex.length > 0 && temperatures[curIndex] > temperatures[trackWaitingIndex.at(-1)]) {
                const waitingIndex = trackWaitingIndex.pop()
                res[waitingIndex] = curIndex - waitingIndex
            }
            trackWaitingIndex.push(curIndex)
        }
        return res;
    }
}
