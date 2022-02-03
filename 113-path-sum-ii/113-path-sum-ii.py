# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def helper(root, target, path):
            if root is None:
                return
            if target == root.val:
                if root.left is None and root.right is None:
                    res.append(path+[root.val])
            helper(root.left, target-root.val, path+[root.val])
            helper(root.right, target-root.val, path+[root.val])
        helper(root, targetSum, [])
        return res