# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def helper(root, pathSum):
            nonlocal totalSum
            if root is None:
                return
            if root.left is None and root.right is None:
                pathSum = 10*pathSum + root.val
                totalSum += pathSum
                return
            helper(root.left, pathSum*10+root.val)
            helper(root.right, pathSum*10+root.val)
        helper(root, 0)
        return totalSum