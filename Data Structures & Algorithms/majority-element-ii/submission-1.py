class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        lst = []
        for i in freq:
            if freq[i]>n//3:
                lst.append(i)
        return lst
        