class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            found = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(count)
                    found = True
                    break
                count += 1            
            if not found:
                res.append(0)
        return res
                
        