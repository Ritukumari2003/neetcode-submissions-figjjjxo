class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = dict()

        for i in range(len(nums)):
            if target-nums[i] in freq:
                return [freq[target-nums[i]], i]
            freq[nums[i]] = freq.get(nums[i], i)
        return None