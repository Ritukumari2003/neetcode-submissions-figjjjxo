
class Solution:
    def kClosest(self, points, k):
        dist_map = {}

        for point in points:
            dist = point[0]**2 + point[1]**2
            dist_map[tuple(point)] = dist

        return sorted(dist_map, key=lambda x: dist_map[x])[:k]