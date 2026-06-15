class Solution:
    # time - O(n log m), space - O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_speed = high

        while low <= high:
            speed = low + (high-low)//2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/speed)
            
            if hour <= h:
                min_speed = speed
                high = speed - 1
            else:
                low = speed + 1
        
        return min_speed
        