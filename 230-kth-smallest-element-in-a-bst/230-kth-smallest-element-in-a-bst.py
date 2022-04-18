# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def helper(root):
            nonlocal k
            nonlocal res
            if root is None:
                return
            helper(root.left)
            
            if k == 1:
                if res is None:
                    res = root.val
                    return
            k -= 1
            helper(root.right)
        helper(root)
        return res