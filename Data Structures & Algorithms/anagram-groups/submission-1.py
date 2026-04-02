from collections import Counter, defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using Sorting
        # mp = dict()

        # for word in strs:
        #     key = ''.join(sorted(word))

        #     if key not in mp:
        #         mp[key] = []

        #     mp[key].append(word)

        # return list(mp.values())

        # Without using sort
        mp = defaultdict(list)

        for word in strs:
            count = [0]*26
            for i in word:
                count[ord(i) - ord('a')] += 1
            mp[str(count)].append(word)

        return list(mp.values())

        
        
        

