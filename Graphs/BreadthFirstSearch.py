
#       1
#     /   \
#    2     3
#   / \   / 
#  4   5 6   
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
root = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node5 = TreeNode(5)
Node6 = TreeNode(6)

root.left = Node2
root.right = Node3

Node2.left = Node4
Node2.right = Node5

Node3.left = Node6


def bfs(root):
    if root is None:
        return []
    
    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    
    return result

print(bfs(root))

