class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        left = 0
        right = len(arr)-1

        while left <= right:
            if right-left+1 == k:
                res = arr[left:right+1]
                return res
            if abs(arr[left]-x) > abs(arr[right]-x): left += 1
            else: right -= 1
        return res



        
        