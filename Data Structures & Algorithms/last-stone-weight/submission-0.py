class Solution:
    # time - O(N log n), space - O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 *  heapq.heappop(heap)
            remaining = x - y
            if (remaining <= 0): continue
            heapq.heappush(heap, -remaining)
        
        if heap:
            return -1 * heap[0]
        else:
            return 0
