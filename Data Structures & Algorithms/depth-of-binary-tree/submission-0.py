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

        max_d = 1

        queue = [(root, 1)]

        while queue:
            node, depth = queue.pop()

            if not node:
                continue

            max_d = max(depth, max_d)

            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))

        return max_d