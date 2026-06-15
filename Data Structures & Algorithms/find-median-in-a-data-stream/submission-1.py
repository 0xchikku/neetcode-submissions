class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap:
            if num > -1 * self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                num = -1 * heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num)
            else:
                num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        
        return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2
        
        