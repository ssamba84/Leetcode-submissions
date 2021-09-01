# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        retavg = 0
        def helper(root):
            nonlocal retavg
            if root is None:
                return (0,0)
            ls, lc = helper(root.left)
            rs, rc = helper(root.right)
            tavg = (ls+rs+root.val)/(lc+rc+1)
            retavg = max(retavg, tavg)
            return ls+rs+root.val, lc+rc+1
        helper(root)
        return retavg
        