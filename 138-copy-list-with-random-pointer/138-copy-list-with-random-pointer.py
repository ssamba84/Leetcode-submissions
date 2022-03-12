"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        prev = None
        copyhead = copyprev = None
        while curr:
            nxt = curr.next
            currcopy = Node(curr.val, next = nxt)
            if copyhead is None:
                copyhead = currcopy
            curr.next = currcopy
            curr = nxt
        curr = head
        while curr:
            currcopy = curr.next
            if currcopy:
                cnext = currcopy.next
            if curr.random:
                currcopy.random = curr.random.next
            if currcopy.next:
                currcopy.next = currcopy.next.next
            curr = cnext
        return copyhead
            
            
            