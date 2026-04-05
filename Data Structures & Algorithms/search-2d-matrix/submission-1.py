class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Using Binary Search
        res = []
        for lst in matrix:
            res.extend(lst)
        low = 0
        high = len(res) - 1
        while low <= high:
            mid = low + (high-low)//2
            if res[mid] == target:
                return True
            elif res[mid] < target:
                low = mid + 1
            else:
                high = mid - 1 
        return False

        
