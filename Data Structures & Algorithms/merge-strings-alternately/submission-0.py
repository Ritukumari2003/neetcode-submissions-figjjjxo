class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        ptr1, ptr2, j = 0,0,0

        while ptr1<len(word1) and ptr2<len(word2):
            res += word1[ptr1]+word2[ptr2]
            ptr1 += 1
            ptr2 += 1
            j += 1
        
        while ptr1<len(word1):
            res += word1[ptr1]
            j += 1
            ptr1 += 1
        
        while ptr2<len(word2):
            res += word2[ptr2]
            j += 1
            ptr2 += 1
        
        return res
        
            
        