# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = math.inf
        q = [(root,1)]
        while len(q)>0:
            node, d = q.pop(0)
            if d >= res:
                continue
            if node.left is None and node.right is None:
                res = min(res, d)
            if node.left:
                q.append((node.left,d+1))
            if node.right:
                q.append((node.right, d+1))
        return res