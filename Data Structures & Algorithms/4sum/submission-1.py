class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # if i > 0 and nums[i-1]==nums[i]:
            #     continue
            for j in range(i+1, len(nums)):
                # if j > 0 and nums[j-1]==nums[j]:
                #     continue
                left = j+1
                right = len(nums)-1
                while left < right:
                    sum_ele = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ele == target:
                        lst = [nums[i], nums[j], nums[left], nums[right]]
                        if lst not in res: res.append(lst)
                        left += 1
                        right -= 1
                        while left<right and nums[left] == nums[left-1]: left += 1
                        while left<right and nums[right] == nums[right+1]: right -= 1
                    elif sum_ele < target:
                        left += 1
                    else:
                        right -= 1
        return res

        




        