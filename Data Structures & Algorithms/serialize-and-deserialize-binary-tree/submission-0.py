# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        results = []
        queue = [root]

        while queue:
            elem = queue.pop()

            if not elem:
                results.append('N')
            else:
                results.append(elem.val)
                queue.append(elem.left)
                queue.append(elem.right)

        return ','.join(str(x) for x in results)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        print(data)
        elems = deque(data.split(','))

        def dfs() -> TreeNode | None:
            elem = elems.popleft()

            if elem != 'N':
                res = TreeNode(int(elem))
                res.right = dfs()
                res.left = dfs()
                return res
            else:
                return None

        return dfs()



