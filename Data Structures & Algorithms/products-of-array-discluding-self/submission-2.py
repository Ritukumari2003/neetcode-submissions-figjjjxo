from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            left = 0
            product = 1
            while i>0 and left < i:
                product *= nums[left]
                left += 1
            right = i+1
            while right < n:
                product *= nums[right]
                right += 1
            res.append(product)
        
        return res


        