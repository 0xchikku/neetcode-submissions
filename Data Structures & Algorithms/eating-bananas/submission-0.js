class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let low = 1
        let high = Math.max(...piles)
        let minSpeed = high
        while (low <= high) {
            const speed = low + Math.floor((high - low)/2)
            let hour = 0
            for (const pile of piles) {
                hour += Math.ceil(pile / speed)
            }
            if (hour <= h) {
                minSpeed = speed
                high = speed - 1
            } else {
                low = speed + 1
            }
        }
        return minSpeed
    }
}
