# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = [root]
        qlen = 1
        while qlen > 0:
            currlen = qlen
            qlen = 0
            currres = []
            for _ in range(currlen):
                node = q.pop(0)
                currres.append(node.val)
                if node.left:
                    qlen += 1
                    q.append(node.left)
                if node.right:
                    qlen += 1
                    q.append(node.right)
            res.append(currres)
        return res