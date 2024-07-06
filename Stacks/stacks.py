

class Stack():
    def __init__(self):
        self.stack = []

    
    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if self.isEmpty():
            return

        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)
    

    def seeStack(self):
        return self.stack

    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
    


myStack = Stack()

myStack.push(3)
myStack.push(3)
myStack.push(3)
myStack.push(3)
myStack.push(3)
myStack.push(3)



print(myStack.seeStack())
    
myStack.pop()
myStack.pop()

print(myStack.seeStack())

myStack.push(5)

print(myStack.pop())