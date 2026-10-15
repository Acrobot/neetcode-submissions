# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 0 -> 1 -> 2 -> 3
        prev = None
        cur = head

        # prev empty
        # cur = 0

        while cur:
            nxt = cur.next   # nxt = 1
            cur.next = prev  # 0 -> None  1 -> 2 -> 3

            prev = cur  # prev = 0
            cur = nxt   # cur = 1

        return prev