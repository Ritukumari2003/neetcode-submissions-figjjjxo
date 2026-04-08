class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        count = 1
        for right in range(len(nums)):
            if count == k:
                max_ele = max(nums[left: right+1])
                res.append(max_ele)
                left += 1
            else: count += 1

        return res