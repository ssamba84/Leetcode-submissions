# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ht = {}
        res = 0
        def helper(root, pathSum):
            nonlocal res
            if root is None:
                return 
            pathSum += root.val
            
            res += ht.get(pathSum-targetSum,0)
            ht[pathSum] = ht.get(pathSum, 0) + 1
            if pathSum == targetSum:
                res += 1
            helper(root.left, pathSum)
            helper(root.right, pathSum)
            ht[pathSum] = ht.get(pathSum, 0) - 1
        helper(root, 0)
        return res