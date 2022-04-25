# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ht = defaultdict(list)
        def dfs(root, r,c):
            if root is None:
                return 
            ht[(r,c)].append(root.val)
            dfs(root.left, r+1, c-1)
            dfs(root.right, r+1, c+1)
        dfs(root, 0,0)
        #print (ht)
        colht = defaultdict(list)
        for ((r,c),v) in ht.items():
            colht[c].append((r,v))
        
        colht = [(c,l) for (c,l) in colht.items()]
        colht.sort(key = lambda x: (x[0]))
        #print (colht)
        res= []
        for _,l in colht:
            l.sort(key = lambda x: x[0])
            tres = []
            for r,v in l:
                tres += v
            res.append(tres)
        return res
        