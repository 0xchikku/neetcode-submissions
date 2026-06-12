class KthLargest:

    # time - O(n log k), space - O(k)
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        print(self.heap)

    # time - O(log k)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        if self.heap:
            return self.heap[0]
        else:
            return 0
