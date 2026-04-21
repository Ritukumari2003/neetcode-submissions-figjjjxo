class Solution:
    def cal_no_of_ships(self, cap, weights):
        days = 1
        curr = 0
        for i in weights:
            if curr + i > cap:
                days += 1
                curr = 0
            curr += i
            
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # linear search : TLE
        # min_cap = max(weights)
        # max_cap = sum(weights)
        # weight = 0
        # for cap in range(min_cap, max_cap+1):
        #     n = self.cal_no_of_ships(cap, weights)
        #     if n<=days:
        #         weight = cap
        #         break
        # return weight

        # binary_search
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = low + (high-low)//2
            n = self.cal_no_of_ships(mid, weights)
            if n<=days:
                high = mid-1
            else:
                low = mid + 1
        return low


        