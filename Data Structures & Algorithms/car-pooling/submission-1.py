
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[1])

        minheap = []   # [end, passengers]
        curr_pass = 0

        for passengers, start, end in trips:

            # Drop passengers
            while minheap and minheap[0][0] <= start:
                drop_end, drop_pass = heapq.heappop(minheap)
                curr_pass -= drop_pass

            # Pick new passengers
            curr_pass += passengers

            if curr_pass > capacity:
                return False

            heapq.heappush(minheap, [end, passengers])

        return True