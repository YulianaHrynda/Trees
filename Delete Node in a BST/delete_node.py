"""Delete Node"""

class TreeNode:
    """TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """Solution"""
    def deleteNode(self, root, key):
        """Delete Node"""
        if not root:
            return None

        if root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            smallest, parent = self.find_smallest(root.right)
            root.val = smallest.val
            if parent:
                parent.left = smallest.right
            else:
                root.right = smallest.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def find_smallest(self, node):
        """Find the smallest value"""
        cur_node = node
        parent = None

        while cur_node.left:
            parent = cur_node
            cur_node = cur_node.left

        return cur_node, parent
