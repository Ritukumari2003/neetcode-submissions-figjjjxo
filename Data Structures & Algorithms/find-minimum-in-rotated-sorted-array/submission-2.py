class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        min_ele = float('inf')
        while low <= high:
            if nums[low] < nums[high]:
                min_ele = min(min_ele, nums[low])
                break
            mid = low + (high-low) // 2
            min_ele = min(min_ele, nums[mid])
            if nums[mid] < nums[low]:
                high = mid - 1
            else:
                low = mid + 1

        return min_ele


        