class MyMinHeap {
    public heap: number[];
    private top: number = 1;
    constructor() {
        this.heap = [0] // for 1 based index
    }

    getMin() {
        return this.heap[this.top]
    }

    getSize() {
        return this.heap.length - 1
    }

    insert(val: number) {
        this.heap.push(val)
        this.percolateUp();
    }

    percolateUp() {
        let i = this.heap.length - 1;
        while (i > 1 && this.heap[i] < this.heap[Math.floor(i/2)]) {
            [this.heap[i], this.heap[Math.floor(i/2)]] = [this.heap[Math.floor(i/2)], this.heap[i]];
            i = Math.floor(i/2);
        }
    }

    remove() {
        const min = this.getMin()
        this.heap[this.top] = this.heap.pop()
        this.percolateDown(this.top)
        return min
    }

    percolateDown(index) {
        while(index < this.heap.length) {
            if (
                (2 * index + 1 < this.heap.length)
                && (this.heap[2*index+1] < this.heap[2*index])
                && (this.heap[index] > this.heap[2*index+1])
            ) {
                [this.heap[index], this.heap[2*index+1]] = [this.heap[2*index+1], this.heap[index]];
                index = 2 * index + 1;
            } else if (
                (2 * index < this.heap.length)
                && (this.heap[index] > this.heap[2*index])
            ) {
                [this.heap[index], this.heap[2*index]] = [this.heap[2*index], this.heap[index]]
                index = 2 * index
            } else {
                break
            }
        }
    }
}

class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    private k: number;
    private minHeap: MyMinHeap;
    constructor(k: number, nums: number[]) {
        this.k = k
        this.minHeap = new MyMinHeap()
        for (const num of nums) {
            this.minHeap.insert(num)
        }
        while (this.minHeap.getSize() > this.k) {
            this.minHeap.remove()
        }
        console.log({heap: this.minHeap.heap})
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val: number): number {
        this.minHeap.insert(val)
        while(this.minHeap.getSize() > this.k) {
            this.minHeap.remove()
        }
        return this.minHeap.getMin()
    }
}
