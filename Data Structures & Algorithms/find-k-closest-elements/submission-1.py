class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = []
        left = 0
        right = len(arr)-1

        while left<=right:
            if right-left+1 == k:
                lst = arr[left:right+1]
                break
            if abs(arr[left]-x) > abs(arr[right]-x):
                left += 1
            else:
                right -= 1
            
        
        return lst



        