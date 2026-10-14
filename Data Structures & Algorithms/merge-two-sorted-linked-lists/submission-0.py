# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2

        first: ListNode | None = None
        res: ListNode | None = None


        while list1 or list2:
            print(f"L1: {list1.val if list1 else None}, L2: {list2.val if list2 else None}")
            if not list2:
                next = list1
                list1 = list1.next
            elif not list1:
                next = list2
                list2 = list2.next
            else:
                if list1.val < list2.val:
                    next = list1
                    list1 = list1.next
                else:
                    next = list2
                    list2 = list2.next

            if not first:
                first = next
                res = next
            else:
                res.next = next
                res = res.next

        return first
