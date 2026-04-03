from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Better Approach : Uses Division method
        n = len(nums)
        product = 1
        for i in nums:
            if i != 0:
                product *= i

        if nums.count(0)>1:
            return [0]*n

        res = []

        for i in range(len(nums)):
            if nums.count(0) == 1:
                res.append(product if nums[i] == 0 else 0)
            else:
                res.append(product // nums[i])

        return res   
        





        