class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    // time - O(1), space - O(1)
    set(key, value, timestamp) {
        if (!this.keyStore.has(key)) this.keyStore.set(key, [])
        this.keyStore.get(key).push([timestamp, value])
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    // time - O(log n), space - O(1)
    get(key, timestamp) {
        let res = ""
        const arr = this.keyStore.get(key)
        if (!arr) return res
        let left = 0
        let right = arr.length - 1
        while (left <= right) {
            const mid = left + Math.floor((right-left)/2)
            if (arr[mid][0] <= timestamp) {
                res = arr[mid][1]
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return res
    }
}
