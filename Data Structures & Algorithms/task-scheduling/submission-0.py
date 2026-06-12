class Solution:
    # time - O(m.n) space - O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            if task not in frequency: frequency[task] = 0
            frequency[task] += 1

        heap = []
        for key, value in frequency.items():
            heapq.heappush(heap, (-value, key))

        queue = deque([])
        step = 0
        while heap or queue:
            step += 1
            if heap:
                value, key = heapq.heappop(heap)
                value += 1
                if value < 0:
                    next = step + n
                    queue.append((next, value, key))
            
            while queue and queue[0][0] <= step:
                next, value, key = queue.popleft()
                heapq.heappush(heap, (value, key))
        
        return step
