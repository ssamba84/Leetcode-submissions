"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or (root.left is None and root.right is None):
            return root
        root.left.next = root.right
        curr = root.left
        while curr.left:
            currlevel = curr
            curr = curr.left
            prev = None
            while currlevel:
                if prev:
                    prev.next = currlevel.left
                currlevel.left.next = currlevel.right
                prev = currlevel.right
                
                currlevel = currlevel.next
        return root