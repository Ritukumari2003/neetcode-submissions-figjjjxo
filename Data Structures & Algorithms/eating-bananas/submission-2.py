class Solution:
    def count_hours_per_pile(self, bananas, piles):
        hours = 0
        for i in piles:
            hours += math.ceil(i/bananas)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Linear Seach : TLE
        # bananas = 0
        # for i in range(1, max(piles)+1):
        #     total_hour = self.count_hours_per_pile(i, piles)
        #     if total_hour <= h
        #         bananas = i
        #         break
        # return bananas

        # Binary Search
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high-low)//2
            if self.count_hours_per_pile(mid, piles) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low


        
            