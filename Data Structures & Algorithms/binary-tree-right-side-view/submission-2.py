# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        levels = {}
        max_depth = 0

        visited = set()

        def dfs(node: Optional[TreeNode], depth=0) -> None:
            nonlocal max_depth

            if not node:
                return

            max_depth = max(max_depth, depth)
            levels[depth] = node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root)

        return [levels[idx] for idx in range(max_depth+1)]