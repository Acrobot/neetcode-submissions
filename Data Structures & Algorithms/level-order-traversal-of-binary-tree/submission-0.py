# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode], output: list[list[int]], level=0) -> None:
        if not root:
            return
        
        if len(output) - 1 < level:
            output.append([])

        output[level].append(root.val)
        self.traverse(root.left, output, level+1)
        self.traverse(root.right, output, level+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        self.traverse(root, levels)

        return levels

