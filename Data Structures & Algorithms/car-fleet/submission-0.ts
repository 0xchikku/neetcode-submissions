class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    // Time - O(n logn), Space - O(n)
    carFleet(target: number, position: number[], speed: number[]): number {
        const noOfCars = position.length;
        const cars = []
        for (let i = 0; i < noOfCars; i++) {
            cars.push({
                position: position[i],
                time: (target - position[i]) / speed[i]
            })
        }
        cars.sort((car1, car2) => car2.position - car1.position)
        const stack = []
        for (let i = 0; i < noOfCars; i++) {
            stack.push(cars[i].time)
            if (stack.length > 1 && stack.at(-2) >= stack.at(-1)) stack.pop()
        }
        return stack.length;
    }
}
