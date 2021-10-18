# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [(root,0, None)]
        depth = parent = None
        while len(q) > 0:
            node, d, p = q.pop(0)
            if (node.val == x) or (node.val == y):
                if depth is None:
                    depth = d
                    parent = p
                else:
                    return (depth == d) and (parent != p)
            else:
                if node.left:
                    q.append((node.left, d+1, node))
                if node.right:
                    q.append((node.right, d+1, node))
        return False