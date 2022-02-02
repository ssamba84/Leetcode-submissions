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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None or (root.left is None and root.right is None):
            return root
        root.left.next = root.right
        lmost = root.left
        while lmost:
            curr = lmost
            lmost = lmost.left
            prev = None
            while curr and curr.left:
                if prev:
                    prev.next = curr.left
                curr.left.next = curr.right
                prev = curr.right
                curr = curr.next
        return root