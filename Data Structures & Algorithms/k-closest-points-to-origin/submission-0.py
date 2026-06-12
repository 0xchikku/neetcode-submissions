class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]
        heap = []
        for point in points:
            distance = ( (point[0] - origin[0])**2 + (point[1] - origin[1])**2 )
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            tupl = heapq.heappop(heap)
            res.append(tupl[1])
        return res