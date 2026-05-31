class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = defaultdict(int)
        curr = 0
        res = 0

        for num in nums:
            prefix_sum[curr] += 1
            curr += num
            res += prefix_sum[curr-k]
        
        return res
        

