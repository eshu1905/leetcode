class MinStack:

    def __init__(self):
        self.stack=[]
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        

    def pop(self) -> None:
        if self.stack:
            k=self.stack[-1]
            self.stack.pop()
            return k
        else:
            return -1

        

    def top(self) -> int:
        k=self.stack[-1]
        return k
        

    def getMin(self) -> int:
        k=min(self.stack)
        return k
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()