class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people)-1

        while left<=right:
            rem = limit-people[right] 
            right -= 1
            boats += 1
            if left <= right and rem >= people[left]:
                left += 1
        return boats 


                    




        