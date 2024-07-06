
#       R
#     /   \
#    A     B
#   / \   / \
#  C   D E   F

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode("R")
NodeA = TreeNode("A")
NodeB = TreeNode("B")
NodeC = TreeNode("C")
NodeD = TreeNode("D")
NodeE = TreeNode("E")
NodeF = TreeNode("F")

root.left = NodeA
root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF


def preOrderTraversal(node):
    if node is None:
        return None
    
    print(node.data)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


def search(node, target):
    if node is None:
        return "null"
    
    elif node.data == target:
        return target
    
    elif node.data > target:
        return search(node.left, target)
    
    else:
        return search(node.right, target)
    

def insert(node, data):
    if node is None:
        return TreeNode(data)
    
    else:
        if node.data > data:
            node.left = insert(node.left, data)

        elif node.data < data:
            node.right = insert(node.right, data)

    return node


def smallestNode(node):
    current = node

    while current is not None:
        current = current.left

    return current.left



