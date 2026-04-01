class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # linear search - O(NlogN)
        # nums.sort()
        # for i in range(len(nums)):
        #     if i>0 and nums[i] == nums[i-1]:
        #         return True
        # return False

        map = dict()

        for i in range(len(nums)):
            if nums[i] in map:
                return True
            map[nums[i]] = map.get(nums[i],0) + 1
        return False



        