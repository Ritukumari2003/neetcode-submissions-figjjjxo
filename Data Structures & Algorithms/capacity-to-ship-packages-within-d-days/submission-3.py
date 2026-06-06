class Solution:

    def cal_min_days(self, n, weights):

        days = 1
        curr = 0

        for ele in weights:
            if curr + ele > n:
                days += 1
                curr = 0
            curr += ele
        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = low+(high-low)//2

            if self.cal_min_days(mid, weights) <= days:
                high = mid-1
            else:
                low = mid+1
        return low