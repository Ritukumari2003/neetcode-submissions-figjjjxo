class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        for i in range(len(nums)):
            c_sum = 0
            for j in range(i, len(nums)):
                c_sum += nums[j]
                if c_sum >= target: 
                    min_len = min(min_len, j-i+1)
                    break
        return 0 if min_len == float('inf') else min_len

        