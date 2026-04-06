class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        lst = nums1
        n = len(lst)
        if n % 2 == 0:
            return (lst[n//2 - 1] + lst[n//2]) / 2
        else:
            return lst[n//2]/1

