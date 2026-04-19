class MinStack:

    def __init__(self):
        self.stack = []
        self.lst = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        ele = self.lst[-1] if self.lst else val
        val = min(val,ele)
        self.lst.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.lst.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.lst[-1]

        
