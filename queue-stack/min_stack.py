class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if val <= self.minVal:
            # Store the old minimum value before updating the minVal
            self.stack.append(self.minVal)
            self.minVal = val
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If the popped value is the current min, pop again to update the minVal
        if val == self.minVal:
            self.minVal = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
