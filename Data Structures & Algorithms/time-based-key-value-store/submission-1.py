class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        data = self.cache[key]
        if not data: return res

        left = 0
        right = len(data) - 1

        while left <= right:
            mid = left + (right-left)//2
            arr = data[mid]

            if arr[0] <= timestamp:
                res = arr[1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
