
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force Approach
        freq = Counter(nums)
        for i in freq:
            if freq[i] >= 2:
                return i
        return 0
        