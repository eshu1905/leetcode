class MyQueue:

    def __init__(self):
        self.queue=[]
        self.size=0
        self.front=0
        self.rear=-1
        

    def push(self, x: int) -> None:
        self.size+=1
        self.rear+=1
        return self.queue.append(x)
    
        

    def pop(self) -> int:
        return self.queue.pop(self.front)
        self.front+=1
        self.size-=1
        
        

    def peek(self) -> int:
        
        return self.queue[0]
        

    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()