class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        i, j = 0, 0
        count = 0
        
        prev = curr = 0
        
        while count <= n // 2:
            prev = curr
            
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            
            count += 1
        
        # Odd length
        if n % 2 == 1:
            return float(curr)
        
        # Even length
        return (prev + curr) / 2