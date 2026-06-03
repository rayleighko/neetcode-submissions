# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # day 1 - watch the solution
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        # if (not p or not q) or (p.val != q.val):
        #     return False
        # return (self.isSameTree(p.left, q.left) and 
        #         self.isSameTree(q.right, q.right))
        
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
        return False

        # day 2 - watch before answer - a little
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(l, r):
            if not l and not r:
                return True
            if not l or not r and (l.val != r.val):
                return False

            return (sameTree(l.left, r.left) and sameTree(l.right, r.right))
        
        if sameTree(root, subRoot):
            return True

        return (sameTree(root.left, subRoot) and sameTree(root.right, subRoot))