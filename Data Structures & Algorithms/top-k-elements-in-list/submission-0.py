class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_list = sorted(freq.items(), key = lambda val: val[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_list[i][0])
        return res
               