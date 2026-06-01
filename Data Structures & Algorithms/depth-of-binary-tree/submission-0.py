# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        d = 1

        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)

        if ld > rd:
            d += ld
        else:
            d += rd

        return d