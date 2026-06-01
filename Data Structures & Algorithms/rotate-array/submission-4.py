class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        res = nums[-k:]+nums[:-k]
        nums[:] = res

        