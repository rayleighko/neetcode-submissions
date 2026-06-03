# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # day 1 - watch the solution
        # DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # BFS
        # if not root:
        #     return 0
        # level = 0
        # q = deque([root])
        # while q:

        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # iterative DFS
        # if not root:
        #     return 0
        # stack = [[root, 1]]
        # res = 1
        
        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         # stack.extend([node.left, node.right])
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res
        
        # day 2 - watch before answer
        # DFS
        # Time complexity: O(n)
        # Space complexity: O(h)
        #   Best Case (balanced tree): O(log(n))
        #   Worst Case (degenerate tree): O(n)
        if not root: 
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))