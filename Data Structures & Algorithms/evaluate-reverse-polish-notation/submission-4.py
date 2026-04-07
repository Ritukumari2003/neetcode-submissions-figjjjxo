class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ans = 0
        for i in tokens:
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if i == '+': ans = a+b
                elif i == '-': ans = b-a
                elif i == '*': ans = a*b
                else: 
                    if b!=0:
                        ans = int(b / a)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[-1]
        