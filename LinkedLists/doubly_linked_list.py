

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 



node1 = Node(3)

node2 = Node(6)
node3 = Node(8)
node4 = Node(12)


node1.next = node2
node1.prev = None 

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = None
node4.prev  = node3


currentNode = node1
while currentNode:
    print(currentNode.data)
    currentNode = currentNode.next

print("null, we reached the end of the linked list")


currentNode = node4

while currentNode:
    print(currentNode.data)
    currentNode = currentNode.prev
print("null")
