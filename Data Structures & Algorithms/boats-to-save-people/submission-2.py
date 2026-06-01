class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count_arr = [0]*((max(people)+1))

        for p in people:
            count_arr[p] += 1

        idx = 0
        for i in range(len(count_arr)):
            if count_arr[i] == 0: continue
            count = count_arr[i]
            while count != 0:
                people[idx] = i
                count -= 1
                idx += 1
        left = 0
        right = len(people)-1
        res = 0

        while left<=right:
            rem = limit - people[right]
            right -= 1
            res += 1
            if left<=right and rem >= people[left]: left += 1
        return res

                    




        