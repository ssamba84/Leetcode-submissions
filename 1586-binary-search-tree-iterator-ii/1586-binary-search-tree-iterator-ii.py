# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.slist = []
        def inorder(root):
            if root is not None:
                inorder(root.left)
                self.slist.append(root.val)
                inorder(root.right)
        inorder(root)
        self.curr = -1
        self.len = len(self.slist)

    def hasNext(self) -> bool:
        return self.curr < self.len-1

    def next(self) -> int:
        self.curr += 1
        ret = self.slist[self.curr]
        return ret

    def hasPrev(self) -> bool:
        return self.curr > 0

    def prev(self) -> int:
        
        self.curr -= 1
        ret = self.slist[self.curr]
        return ret


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()