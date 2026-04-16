class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, right = 0, 0
        c_sum = 0
        min_len = float('inf')
        while right<len(nums): 
            c_sum += nums[right]           
            if c_sum >= target:
                while c_sum >= target:
                    min_len = min(min_len, right-left+1)
                    c_sum -= nums[left]
                    left += 1
            right += 1
                
        return 0 if min_len == float('inf') else min_len
