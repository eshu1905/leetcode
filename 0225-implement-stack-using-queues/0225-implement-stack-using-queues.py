class MyStack:

    def __init__(self):
        self.stack=[]
        self.size=0
       
        
        

    def push(self, x: int) -> None:
        self.size+=1
        return self.stack.append(x)

        

    def pop(self) -> int:
        self.size-=1
        return self.stack.pop()
        

    def top(self) -> int:
        k=self.stack[-1]
        return k
        

    def empty(self) -> bool:
        if  not self.size:
            return True
        else:
            return False    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()