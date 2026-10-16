# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0

        last = head
        while last.next:
            last = last.next
            length += 1

        cur = head
        prev = None
        while length - n >= 0:
            prev = cur
            cur = cur.next
            length -= 1

        print(f"prev: {prev.val if prev else None}, cur: {cur.val}")

        # A -> B -> C -> D
        # n = 2
        # last = D
        # 4-2 
        
        nxt = cur.next
        if not prev:
            head = nxt
        else:
            prev.next = nxt

        return head

        