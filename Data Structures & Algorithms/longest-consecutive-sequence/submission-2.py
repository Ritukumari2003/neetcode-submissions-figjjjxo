class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Without using sorting : Will not work for arrays with negative elements
        # if not nums:
        #     return 0
        # max_ele = max(nums)
        # res = [0]*(max_ele+1)
        # for i in nums:
        #     res[i] += 1
        # count = 0
        # max_seq = 0
        # for i in range(len(res)):
        #     if res[i] > 0:
        #         count += 1
        #     else:
        #         count = 0
        #     max_seq = max(max_seq, count)
        # return max_seq

        num_set = set(nums)
        max_seq = 0

        for num in num_set:
            # start of sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                max_seq = max(max_seq, count)

        return max_seq




        