"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ht = {}
        def helper(node):
            if node is None:
                return None
            if node.val in ht:
                return ht[node.val]
            retnode = Node(node.val, [])
            ht[node.val] = retnode
            for nei in node.neighbors:
                retnode.neighbors.append(helper(nei))
            return retnode
        return helper(node)
            