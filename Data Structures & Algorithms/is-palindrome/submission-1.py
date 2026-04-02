class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute Force Approach
        # s1 = ""
        # for i in s:
        #     if i.isalnum():
        #         s1 += i.lower()
        # return s1 == s1[::-1]

        # Optimal Approach

        low = 0
        high = len(s)-1

        while low<=high:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        
        return True
        