class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = self.getMin()
        if minVal == None or val <= minVal:
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1] if len(self.min) > 0 else None
