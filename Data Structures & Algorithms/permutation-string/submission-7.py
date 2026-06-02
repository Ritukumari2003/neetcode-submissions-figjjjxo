class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1): return False

        left = 0
        for right in range(len(s2)):
            if right-left+1 == len(s1):
                if Counter(s1) == Counter(s2[left:right+1]): return True
                left += 1
        return False
                