# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        if not root:
            return 0

        def height(node: TreeNode) -> int:
            nonlocal max_d

            if not node:
                return 0

            l_height = height(node.left)
            r_height = height(node.right)

            max_d = max(max_d, l_height + r_height)

            return 1 + max(l_height, r_height)
            
        height(root)

        return max_d
        