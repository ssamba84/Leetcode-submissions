# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return (-math.inf, -math.inf)
            lps, lmx = helper(root.left)
            rps, rmx = helper(root.right)
            lps = max(0,lps)
            rps = max(0,rps)
            return (root.val+max(lps,rps), max(lmx, rmx, root.val + lps+rps))
        return helper(root)[1]