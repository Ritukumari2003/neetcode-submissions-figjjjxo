class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ele_sum = 0
        lst = []
        for i in operations:
            if i=="+":
                lst.append(lst[-1]+lst[-2])
            elif i=="D":
                lst.append(2*lst[-1])
            elif i=="C":
                if lst: lst.pop()
            else: lst.append(int(i))
        return sum(lst)


        