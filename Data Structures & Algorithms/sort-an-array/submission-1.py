class Solution:
    def quick_sort(self, nums):
        n = len(nums)

        if n <= 0: return nums

        pivot = nums[n//2]
        left = [x for x in nums if x<pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x>pivot]

        return self.quick_sort(left) + mid + self.quick_sort(right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)