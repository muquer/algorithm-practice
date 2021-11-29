'''
Returns the depth/height of a binary tree
'''
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def find_height(root : Node, height : int=0):
    if root is None: return height
    return max(find_height(root.left, height+1), find_height(root.right, height+1))