class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        freq = Counter(t)
        window = Counter()
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window >= freq:
                while window[s[left]] > freq[s[left]]:
                    window[s[left]] -= 1
                    left += 1
                if not res or (right-left+1) < len(res):
                    res = s[left: right+1]
        return res if res else ""

            

        
                    





        