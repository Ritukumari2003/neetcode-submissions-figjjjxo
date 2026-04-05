class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        i = 0

        while i < len(s):
            if s[i] in '[{(':
                stack.append(s[i])
            elif stack and ((s[i] == ')' and stack[-1] == '(') or (s[i] == '}' and stack[-1] == '{') or (s[i] == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                return False
            i+=1
        return True if len(stack) == 0 else False         
            

        
        