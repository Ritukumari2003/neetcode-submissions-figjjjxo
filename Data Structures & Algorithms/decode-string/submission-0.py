class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch != ']':
                stk.append(ch)
            else:
                str1 = ''
                while stk[-1] != '[':
                    str1 = stk.pop() + str1
                stk.pop()
                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num)* str1)
        return ''.join(stk)
        