# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if root is None:
            return ans
        def helper(root, prev):
            nonlocal ans
            if root is None:
                return
            if root.val >= prev:
                ans += 1
            helper(root.left, max(prev,root.val))
            helper(root.right, max(prev,root.val))
        helper(root, root.val)
        return ans