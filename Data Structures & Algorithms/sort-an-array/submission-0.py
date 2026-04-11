class Solution:
    def quick_sort(self, nums):
        n = len(nums)
        if n<=0: return nums

        pivot = nums[n//2]
        left_sorted = [x for x in nums if x < pivot]
        mid_sorted = [x for x in nums if x == pivot]
        right_sorted = [x for x in nums if x > pivot]
        
        return self.quick_sort(left_sorted) + mid_sorted + self.quick_sort(right_sorted)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)