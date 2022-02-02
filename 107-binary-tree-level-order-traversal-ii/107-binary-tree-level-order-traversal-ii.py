# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = [root]
        qlen = 1
        while len(q) > 0:
            clen = qlen
            qlen = 0
            curres = []
            for _ in range(clen):
                node = q.pop(0)
                curres.append(node.val)
                if node.left:
                    q.append(node.left)
                    qlen += 1
                if node.right:
                    q.append(node.right)
                    qlen += 1
            res.append(curres)
        return res[::-1]