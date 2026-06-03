class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        paths = path.split('/')

        for i in paths:
            if i == '..':
                if stk : stk.pop()
            elif i != '.' and i != '': stk.append(i)
        return '/'+'/'.join(stk)


        