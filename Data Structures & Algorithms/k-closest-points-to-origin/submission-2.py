
class Solution:
    def kClosest(self, points, k):
        minheap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            minheap.append([dist, point[0], point[1]])

        heapq.heapify(minheap)
        res = []
        for _ in range(k):
            curr = heapq.heappop(minheap)
            res.append([curr[1], curr[2]]) 
        return res


        