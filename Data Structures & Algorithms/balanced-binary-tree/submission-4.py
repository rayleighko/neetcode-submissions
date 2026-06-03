# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # day 1 - watch solution
        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balance = (left[0] and right[0] and
        #                abs(left[1] - right[1]) <= 1)

        #     return [balance, 1 + max(left[1], right[1])]

        # return dfs(root)[0]
        # day 2 - watch before answer
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            diff = abs(left[1] - right[1])
            balance = (left[0] and right[0] and diff <= 1)

            return [balance, 1 + max(left[1], right[1])]

        bal = dfs(root)[0]
        
        return bal