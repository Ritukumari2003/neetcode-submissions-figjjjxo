class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for i in freq:
            if freq[i] > 1: return True
        return False


        