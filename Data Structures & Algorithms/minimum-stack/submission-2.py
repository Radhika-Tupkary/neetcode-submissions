class MinStack:

    def __init__(self):
        self.stack1 = []    # original order
        self.stack2 = []    # stores the minimum so far at each level.

    def push(self, val: int) -> None:
        self.stack1.append(val)

        if self.stack2:
            if self.stack2[-1] >= val:
                self.stack2.append(val)
        else:
            self.stack2.append(val)

    def pop(self) -> None:
        if self.stack1:
            if self.stack2:
                if self.stack1[-1] == self.stack2[-1]:
                    self.stack2.pop()
            self.stack1.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        
