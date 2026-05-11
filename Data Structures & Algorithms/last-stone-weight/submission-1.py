class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Creating max heap
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)

            if max2 > max1: 
                rem = max1 - max2
                heapq.heappush(stones, rem)
        return -stones[0] if stones else 0


        
        