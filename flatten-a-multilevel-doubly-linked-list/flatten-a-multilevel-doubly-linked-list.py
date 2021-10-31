"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        stk = []
        while curr or len(stk) != 0:
            if curr is None:
                curr = stk.pop()
                cprev.next = curr
                curr.prev = cprev
            cprev = curr
            if curr.child:
                if curr.next:
                    stk.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            curr = curr.next
        curr = head
        return head