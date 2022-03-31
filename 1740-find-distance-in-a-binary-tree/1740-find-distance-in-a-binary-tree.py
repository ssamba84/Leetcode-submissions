# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        if p == q:
            return 0
        def findcommonancestor(root, p,q):
            if root is None:
                return (None,0)
            
            ln,lf = findcommonancestor(root.left, p, q)
            rn,rf = findcommonancestor(root.right, p, q)
            if (lf == 1 and rf ==1):# or (((rf+lf) == 1) and (root.val in [p,q])):
                return (root, 2)
            if (root.val == p or root.val== q):
                if lf+rf == 1:
                    return (root, 2)
                else:
                    return (None, 1)
            
            
            if lf == 2:
                return (ln,2)
            if rf == 2:
                return (rn,2)
            return (None,(lf+rf))
            
        n,c = findcommonancestor(root, p, q)
        def finddist(root, val):
            q = [(root,0)]
            while len(q) > 0:
                node, res = q.pop(0)
                if node.val == val:
                    return res
                if node.left:
                    q.append((node.left, res+1))
                if node.right:
                    q.append((node.right, res+1))
            return -1
        return finddist(n, p)+finddist(n,q)
                