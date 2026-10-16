"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        storage = defaultdict(lambda: Node(0))
        storage[None] = None

        cur = head
        while cur:
            storage[cur].val = cur.val
            storage[cur].next = storage[cur.next]
            storage[cur].random = storage[cur.random]
            cur = cur.next

        return storage[head]
            