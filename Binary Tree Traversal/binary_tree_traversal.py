"""
Binary Tree Traversal
"""

class Node:
    """Node"""
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    """Pre-order traversal"""
    result = []
    if node is None:
        return result

    result.append(node.data)
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))

    return result

# In-order traversal
def in_order(node):
    """In-order traversal"""
    result = []
    if node is None:
        return result

    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))

    return result

# Post-order traversal
def post_order(node):
    """Post-order traversal"""
    result = []
    if node is None:
        return result

    result.extend(post_order(node.left))
    result.extend(post_order(node.right))
    result.append(node.data)

    return result
