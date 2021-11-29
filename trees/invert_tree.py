'''
Mirrors a binary tree horizontally
'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root : Node):
    if root is None: return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root