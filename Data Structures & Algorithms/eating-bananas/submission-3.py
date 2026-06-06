class Solution:

    def count_piles(self, n, piles):
        i = 0

        for ele in piles:
            i += math.ceil(ele/n)
        return i

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low<=high:
            mid = low + (high-low)//2
            if self.count_piles(mid, piles) <= h:
                high = mid-1
            else:
                low = mid+1
        return low
        


        
            