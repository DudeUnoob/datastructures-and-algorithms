

class Node():
    def __init__(self, data):

        self.data = data 
        self.next = None


node1 = Node(3)
node2 = Node(4)
node3 = Node(8)
node4 = Node(10)
node5 = Node(16)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


currentNode = node1

while currentNode:
    print(currentNode.data, )
    currentNode = currentNode.next