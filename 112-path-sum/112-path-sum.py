# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def helper(root, target):
            if root is None:
                return False
            if root.val == target:
                if root.left is None and root.right is None:
                    return True
            return helper(root.left, target-root.val) or helper(root.right, target-root.val)
        return helper(root, targetSum)