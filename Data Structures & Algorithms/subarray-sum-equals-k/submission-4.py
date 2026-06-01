class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = {0:1}
        curr = 0
        res = 0

        for num in nums:
            curr += num

            if curr-k in prefix_sum:
                res += prefix_sum[curr-k]
            prefix_sum[curr] = prefix_sum.get(curr, 0) + 1
        
        return res
        

