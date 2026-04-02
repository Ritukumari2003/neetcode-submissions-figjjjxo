class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force Approach
        # res = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             t_sum = nums[i] + nums[j] + nums[k]
        #             if t_sum == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 res.add(tuple(triplet))
    
        # return [list(x) for x in res]

        # Better Approach
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums)-1

            while left<right:
                t_sum = nums[i] + nums[left] + nums[right]
                if t_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif t_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
                
                




