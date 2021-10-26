# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        if root is None:
            return 0
        def helper(root, d):
            nonlocal res
            if root is None:
                return
            if root.left is None and root.right is None:
                res = min(res, d+1)
            helper(root.left, d+1)
            helper(root.right, d+1)
        helper(root, 0)
        return res