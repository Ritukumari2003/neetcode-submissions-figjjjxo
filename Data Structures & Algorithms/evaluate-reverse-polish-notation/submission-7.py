class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ans = 0
        ops = ['+', '-', '*', '/']
        i = 0
        while i<len(tokens):
            if tokens[i] in ops:
                a = stk.pop()
                b = stk.pop()
                if tokens[i] == '+': 
                    ans = a+b
                elif tokens[i] == '-':
                    ans = b-a
                elif tokens[i] == '*':
                    ans = a*b
                else: ans = int(b / a)
                stk.append(ans)
            else: stk.append(int(tokens[i]))
            i += 1
        return stk[-1]




        