# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        q = [(root, None)]

        while q:
            elem, max_val = q.pop()
            if not elem:
                continue

            if not max_val or elem.val >= max_val:
                good += 1
            
            if max_val:
                max_val = max(max_val, elem.val)
            else:
                max_val = elem.val
                
            q.append((elem.left, max_val))
            q.append((elem.right, max_val))

        return good