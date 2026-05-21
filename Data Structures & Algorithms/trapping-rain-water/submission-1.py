class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0        
        
        for i in range(len(height)):
            max_left = height[i]
            max_right = height[i]

            j = 0
            while j<i:
                max_left = max(max_left, height[j])
                j += 1
            j = i+1
            while j<len(height):
                max_right = max(max_right, height[j])
                j += 1
            
            res += min(max_left, max_right) - height[i]
        
        return res



