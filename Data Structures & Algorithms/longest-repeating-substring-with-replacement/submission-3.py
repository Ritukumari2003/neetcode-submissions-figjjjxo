class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        left = 0
        right = 0
        max_freq = 0
        count = {}

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            length = right-left+1
            if length - max_freq <= k:
                max_len = max(max_len, length)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
        return max_len





        


