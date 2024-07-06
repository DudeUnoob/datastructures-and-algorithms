

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return
        
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    



myQueue = Queue()

myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)

myQueue.peek()

print(myQueue.queue)
print(myQueue.peek())
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.queue)

print(myQueue.isEmpty())
print(myQueue.size())