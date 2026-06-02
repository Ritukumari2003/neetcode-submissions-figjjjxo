class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_map = dict()

        max_len = 0
        left = 0
        
        for right in range(len(s)):
            ch_map[s[right]] = ch_map.get(s[right], 0) + 1
                
            while ch_map[s[right]] > 1:
                ch_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
        