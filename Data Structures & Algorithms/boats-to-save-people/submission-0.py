class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        
        left = 0
        right = len(people)-1
        sum_ele = 0
        while left <= right:
            rem_weight = limit - people[right]
            right -= 1
            sum_ele += 1
            if left<=right and rem_weight >= people[left]:
                left += 1
        return sum_ele
                    




        