class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force Approach
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                min_height = min(heights[i], heights[j])
                area = min_height * (j-i)
                res = max(res, area)
        return res        