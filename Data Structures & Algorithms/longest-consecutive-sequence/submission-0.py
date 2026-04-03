class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using sorting
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        max_seq = float('-inf')
        for i in range(len(nums)):
            if i>0:
                if nums[i] == nums[i-1]+1:
                    count += 1
                else:
                    count = 1
            max_seq = max(max_seq, count)

        return max_seq        
        