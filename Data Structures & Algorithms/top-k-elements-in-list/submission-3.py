class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        lst = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        
        res = []
        for i in range(k):
            res.append(lst[i][0])
        return res 