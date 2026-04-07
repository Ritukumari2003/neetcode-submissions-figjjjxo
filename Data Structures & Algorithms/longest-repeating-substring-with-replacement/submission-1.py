class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(s)):
            count = {}
            max_freq = 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                
                length = j-i+1

                if length - max_freq <= k:
                    max_len = max(max_len, length)
            
        return max_len


