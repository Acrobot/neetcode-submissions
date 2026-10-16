# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = head
        slow = head

        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next

            slow = slow.next

        # A -> B -> C
        cur = slow  # cur = A
        prev = None # prev = None

        while cur:
            print(f"cur: {cur.val}, nxt: {cur.next.val if cur.next else None}, prev: {prev.val if prev else None}")
            nxt = cur.next  # nxt = B
            cur.next = prev # A -> None  B -> C
            prev = cur      # prev = A
            cur = nxt       # cur = B

        left = head
        right = prev

        while left or right:
            # print(f"l: {left.val if left else None}, r: {right.val if right else None}")
            # print(f"l_n: {left.next.val if left.next else None}, r_n: {right.next.val if right.next else None}")
            if left:
                l_next = left.next
                left.next = right
                left = l_next

            if right:
                r_next = right.next
                right.next = l_next
                right = r_next