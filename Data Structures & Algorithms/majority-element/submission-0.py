class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = float('-inf')
        max_freq_ele = float('-inf')
        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_freq_ele = i
        return max_freq_ele

        