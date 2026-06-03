class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []

        for i in range(len(asteroids)):
            alive = True

            while alive and stk and stk[-1] > 0 and asteroids[i] < 0:
                if stk[-1] == -asteroids[i]: 
                    alive = False
                    stk.pop()
                elif stk[-1] < abs(asteroids[i]):
                    stk.pop()
                else:
                    alive = False
            if alive:
                stk.append(asteroids[i])
        return stk            

        