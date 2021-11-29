'''
Binary tree and common operations
'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def inorder(root : Node):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def insert(root : Node, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)

    if value > root.value:
        root.right = insert(root.right, value)
    
    return root


def search(root: Node, value):
    if root is None:
        return None

    if root.value == value:
        return root
    elif  value < root.value:
        return search(root.left, value)
    elif value > root.value:
        return search(root.right, value)
