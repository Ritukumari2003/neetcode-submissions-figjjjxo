class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        if len(arr) == 0: return 0
        max_len = 1
        left = 0
        for right in range(1,len(arr)):
            if arr[right] == arr[right-1] + 1:
                max_len = max(max_len, right-left+1)
            else:
                left = right
        return max_len
        
 
