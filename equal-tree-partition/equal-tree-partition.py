# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def filltree(root):
            if root is None:
                return 0
            ls = filltree(root.left)
            rs = filltree(root.right)
            root.val += ls+rs
            return root.val
        filltree(root)
        totalsum = root.val
        ROOT = root
        def helper(root):
            nonlocal totalsum
            nonlocal ROOT
            if root is None:
                return False
            return (root!= ROOT and totalsum == 2*(totalsum-root.val)) or helper(root.left) or helper(root.right)
        return helper(root)
            