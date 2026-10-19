class Solution:
    def rightSideView(
        self,
        root: Optional[TreeNode],
    ) -> list[int]:
        if not root:
            return []

        rightmost = {}
        max_depth = 0

        q = [(root, 0)]
        while q:
            node, level = q.pop()
            if not node:
                continue

            max_depth = max(max_depth, level)
            rightmost[level] = node

            q.append((node.right, level+1))
            q.append((node.left, level+1))

        return [rightmost[level].val for level in range(max_depth+1)]