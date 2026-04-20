class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.minStack.append(val)
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)
            self.minStack.append(self.minVal)

        self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minVal = self.minStack[-1] if self.minStack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
        
