
# Example binary search tree
#
#       50
#     /    \
#   30      70
#  / \     /  \
# 20 40   60  80



class TreeNode():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None



root = TreeNode(50)
node30 = TreeNode(30)
node20 = TreeNode(20)
node40 = TreeNode(40)
node70 = TreeNode(70)
node60 = TreeNode(60)
node80 = TreeNode(80)

root.left = node30
root.right = node70

node30.left = node20
node30.right = node40

node70.left = node60
node70.right = node80


def search(node, target):
    if node is None:
        return
    
    if node.data == target:
        return "found"
    
    elif node.data > target:
        return search(node.left, target)
    
    else:
        return search(node.right, target)
    

    
    
    

def smallestNode(node):
    current = node

    while current is not None:
        current = current.left

    return current.data


def insert(node, data):
    if node is None:
        return
    
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        
        elif data > node.data:
            node.right = insert(node.right, data)

    return node



print(search(root, 30), "hello")
print(smallestNode(root))
print(insert(root, 5000))



def preOrderTraversal(node = root):
    if node is None:
        return
    
    print(node.data)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


print(preOrderTraversal())



def add(node, data):
    if node is None:
        return TreeNode(data)
    
    else:
        if data > node.data:
            node.right = add(node.right, data)

        else:
            node.left = add(node.left, data)

    return node

