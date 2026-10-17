"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()

        queue: list[Node] = [node]
        returned = {}

        while queue:
            element = queue.pop()

            if element.val in visited:
                continue

            visited.add(element.val)

            if element.val not in returned:
                    returned[element.val] = Node(element.val)

            for neighbor in element.neighbors:
                queue.append(neighbor)

                if neighbor.val not in returned:
                    returned[neighbor.val] = Node(neighbor.val)

                returned[element.val].neighbors.append(returned[neighbor.val])

        return returned[1]


