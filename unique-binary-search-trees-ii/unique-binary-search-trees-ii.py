# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(l,r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            ret = []
            for i in range(l,r+1):
                ltrees = helper(l,i-1)
                rtrees = helper(i+1,r)
                for lt in ltrees:
                    for rt in rtrees:
                        root = TreeNode(i, lt, rt)
                        ret.append(root)
            return ret
        return helper(1,n)
        
                        
                