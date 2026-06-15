class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for num in nums:
            minheap.append(num)
            heapq.heapify(minheap)
            if len(minheap)>k: heapq.heappop(minheap)
        return minheap[0]