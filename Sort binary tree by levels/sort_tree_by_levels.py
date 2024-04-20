"""
Sort Tree by Levels
"""
from collections import deque

class Node:
    """Node"""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    """Tree by levels"""
    if not node:
        return []
    result = []
    queue = deque([node])

    while queue:
        cur_node = queue.popleft()
        result.append(cur_node.value)

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

    return result
