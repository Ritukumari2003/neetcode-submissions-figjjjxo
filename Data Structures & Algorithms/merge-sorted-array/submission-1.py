class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # pointers for nums1
        left = m-1
        right = m+n-1

        # pointers for nums2 
        ptr = n-1

        while left>=0 and ptr>=0:
            if nums1[left]>nums2[ptr]: 
                nums1[right] = nums1[left]
                left -= 1
            else:
                nums1[right] = nums2[ptr]
                ptr -= 1
            right -= 1
        while ptr >= 0:
            nums1[right] = nums2[ptr]
            ptr -= 1
            right -= 1

        
