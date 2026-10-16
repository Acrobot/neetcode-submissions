# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  1  2  3
        #     1  5
        #  1  3  8

        #  1  2         8
        #     1         5
        #  1   3(+1)   3(1)
        
        output = ListNode()
        tail = output

        remainder = 0
        while l1 or l2 or remainder:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            if s > 9:
                s -= 10
                remainder = 1
            else:
                remainder = 0

            
            output.val = s

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            if l1 or l2 or remainder:
                new_node = ListNode()
                output.next = new_node
                output = new_node  

        return tail
