class MyQueue:

    def __init__(self):
        self.inStack  = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.fillOutStack()
        return self.outStack.pop()


    def peek(self) -> int:
        self.fillOutStack()
        return self.outStack[-1]


    def empty(self) -> bool:
        return not self.inStack and not self.outStack

    def fillOutStack(self) -> None:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
