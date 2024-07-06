
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    

root = TreeNode(1)
two = TreeNode(2)
twoTwo = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
fourFour = TreeNode(4)
threeThree = TreeNode(3)

root.left = two
root.right = twoTwo

two.left = three
two.right = four

twoTwo.left = fourFour
twoTwo.right = threeThree


def preOrderTraversal(node):
    if node is None:
        return

    if node.left != node.right:
        return False
    
    print(node.data)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


# print(preOrderTraversal(root))



def pre_order_traversal(tree, index, result=None):
    if result is None:
        result = []
    if index < len(tree):
        result.append(tree[index])  # Node itself
        pre_order_traversal(tree, 2*index + 1, result)  # Left child
        pre_order_traversal(tree, 2*index + 2, result)  # Right child
    return result


print(pre_order_traversal([1,2,2,3,4,4,3], 0))
