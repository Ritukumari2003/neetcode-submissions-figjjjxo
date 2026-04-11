class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*3
        for i in nums:
            res[i] += 1
        
        j = 0
        for i in range(3):
            while res[i]!=0:
                res[i] -= 1
                nums[j] = i
                j += 1
        


        